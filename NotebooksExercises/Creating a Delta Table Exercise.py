# Databricks notebook source


# COMMAND ----------

# MAGIC %md
# MAGIC CHETADO

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC USE SCHEMA testva_schema;
# MAGIC
# MAGIC select current_catalog(),current_schema();
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC SELECT *
# MAGIC FROM read_files(
# MAGIC   '/Volumes/test_va/testva_schema/va_storage/Empleados_Mockaroo.csv',
# MAGIC   format => 'csv',
# MAGIC   header => true,
# MAGIC   inferSchema => true
# MAGIC )
# MAGIC

# COMMAND ----------

# MAGIC %md
# MAGIC CREAR LA TABLA DELTA

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 1. Eliminamos la tabla si ya existe para evitar conflictos
# MAGIC DROP TABLE IF EXISTS employees_data;
# MAGIC
# MAGIC -- 2. Creamos la tabla Delta leyendo el CSV desde el Volume
# MAGIC CREATE TABLE employees_data AS
# MAGIC SELECT 
# MAGIC     id,
# MAGIC     first_name,
# MAGIC     last_name,
# MAGIC     email,
# MAGIC     gender,
# MAGIC     ip_address
# MAGIC FROM read_files(
# MAGIC   '/Volumes/test_va/testva_schema/va_storage/Empleados_Mockaroo.csv',
# MAGIC   format => 'csv',
# MAGIC   header => true,
# MAGIC   inferSchema => true
# MAGIC );
# MAGIC
# MAGIC -- 3. Verificamos el contenido
# MAGIC SELECT * FROM employees_data;

# COMMAND ----------



# COMMAND ----------

# MAGIC %sql
# MAGIC --DESCRIBE EXTENDED employees_data
# MAGIC --DESCRIBE detail employees_data
# MAGIC
# MAGIC DESCRIBE HISTORY employees_data

# COMMAND ----------

# MAGIC %sql
# MAGIC INSERT INTO employees_data (id, first_name, last_name, email, gender, ip_address)
# MAGIC VALUES (9999, 'Laura', 'Smith', 'lsmith@example.com', 'Female', '192.168.1.1');
# MAGIC
# MAGIC UPDATE employees_data
# MAGIC SET email = 'new.email@example.com'
# MAGIC WHERE id = 13;
# MAGIC
# MAGIC DELETE FROM employees_data
# MAGIC WHERE id = 19;

# COMMAND ----------

# MAGIC %sql
# MAGIC -- 3. Verificamos el contenido
# MAGIC SELECT * FROM employees_data;

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table test_va.testva_schema.employees_data
