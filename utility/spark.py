from pyspark.sql import SparkSession, HiveContext

def get_Spark_Session(nome):
    spark=(SparkSession.builder.appName(nome).enableHiveSupport().getOrCreate())
    return spark