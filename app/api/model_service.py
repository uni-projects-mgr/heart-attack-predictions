import json
from pyspark.sql import SparkSession
from pyspark.ml.feature import VectorAssembler, MinMaxScaler
from pyspark.ml.classification import RandomForestClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator, BinaryClassificationEvaluator, RegressionEvaluator
from pyspark.sql.types import StructType, StructField, FloatType
import findspark

findspark.init()

class ModelService:
    def __init__(self, path: str):
        self.spark = SparkSession.builder.appName("ModelService").getOrCreate()
        self.data = self.spark.read.csv(path, header=True, inferSchema=True)
        print("ModelService initialized")

    def build_and_evaluate(self) -> dict:
        print("Building model...")
        assembler = VectorAssembler(inputCols=self.data.columns[:-1], outputCol="features")
        assembled_data = assembler.transform(self.data)

        scaler = MinMaxScaler(inputCol="features", outputCol="scaled_features")
        scaled_data = scaler.fit(assembled_data).transform(assembled_data)

        train_data, test_data = scaled_data.randomSplit([0.8, 0.2])

        model = RandomForestClassifier(featuresCol="scaled_features", labelCol="output", numTrees=100)
  
        fitted_model = model.fit(train_data)

        self.model = fitted_model

        print("Evaluating model...")
        predictions = fitted_model.transform(test_data)

        evaluator = MulticlassClassificationEvaluator(labelCol="output", predictionCol="prediction")
        auc_evaluator = BinaryClassificationEvaluator(labelCol="output")
        mae_rmse_evaluator = RegressionEvaluator(labelCol="output")

        accuracy = evaluator.evaluate(predictions, {evaluator.metricName: "accuracy"})
        loss = evaluator.evaluate(predictions, {evaluator.metricName: "logLoss"})
        auc = auc_evaluator.evaluate(predictions)
        mae = mae_rmse_evaluator.evaluate(predictions, {mae_rmse_evaluator.metricName: "mae"})
        rmse = mae_rmse_evaluator.evaluate(predictions, {mae_rmse_evaluator.metricName: "rmse"})

        results = {
            "accuracy": accuracy,
            "loss": loss,
            "auc": auc,
            "mae": mae,
            "rmse": rmse
        }

        print(results)
        return results

    def classify(self, sample) -> json:
        print("Classifying sample: ", sample, flush=True)
        schema = StructType([StructField(key, FloatType(), True) for key in sample.keys()])
        data = [tuple(sample.values())]
        df = self.spark.createDataFrame(data, schema=schema)

        assembler = VectorAssembler(inputCols=list(sample.keys()), outputCol="scaled_features")
        df_assembled = assembler.transform(df)

        result = self.model.transform(df_assembled)

        predicted_output = result.select("prediction").collect()[0][0]

        return {
            "prediction": int(predicted_output)
        }
