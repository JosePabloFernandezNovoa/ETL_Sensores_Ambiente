# ETL_Sensores_Ambiente

Claro, aquí tienes la estructura del README para tu proyecto de Sistema de Monitorización de Ambiente en GitHub:

---

# Sistema de Monitorización de Ambiente

## Descripción General

Hemos implementado un sistema integral de monitorización ambiental que mide cuatro parámetros clave: temperatura, ruido, humedad y luminosidad. Este sistema está basado en una red de sensores conectados a un Arduino y se integra con una Raspberry Pi que corre Node-RED para la gestión y envío de datos.

## Arquitectura del Sistema

### Sensores y Arduino

- **Sensores**: Utilizamos sensores específicos para medir la temperatura, el ruido, la humedad y la luminosidad.
- **Arduino**: Los sensores están conectados a un Arduino, que se encarga de leer los valores y enviarlos a la Raspberry Pi.

### Raspberry Pi y Node-RED

- **Raspberry Pi**: Actúa como el puente entre el Arduino y el sistema de procesamiento de datos.
- **Node-RED**: Es una herramienta de programación visual que facilita la integración de hardware, APIs y servicios en línea. En nuestro caso, Node-RED recibe los datos del Arduino y, mediante un script en Python, actúa como un productor de Kafka.

### Kafka

- **Productor de Kafka**: El script de Python en Node-RED toma los datos de los sensores y los envía a un topic específico en un clúster de Kafka. Este proceso asegura que los datos sean entregados de manera eficiente y en tiempo real.
- **Topic de Kafka**: Es un canal lógico donde se publican los datos. Cada sensor tiene su propio topic o se pueden agrupar en un único topic dependiendo de la configuración.

### Centro de Procesamiento de Datos (CPD)

- **Consumidores de Kafka**: En una máquina del CPD, hemos configurado varios consumidores de Kafka que se encargan de suscribirse a los topics correspondientes y recibir los datos en tiempo real.
- **Procesamiento de Datos**: Los consumidores procesan los datos para prepararlos para el almacenamiento, realizando tareas como limpieza, agregación y transformación según sea necesario.

### Sistema de Almacenamiento HDFS

- **HDFS (Hadoop Distributed File System)**: Es el sistema de almacenamiento donde se guardan los datos procesados. Contamos con una configuración que incluye un namenode y cinco datanodes, lo que asegura alta disponibilidad y redundancia.
  - **Namenode**: Es el nodo maestro que gestiona el sistema de archivos y regula el acceso a los archivos.
  - **Datanodes**: Son los nodos que realmente almacenan los datos. En nuestro sistema, tenemos cinco datanodes que garantizan la distribución y replicación de los datos para mejorar la tolerancia a fallos y la capacidad de almacenamiento.

## Flujo de Datos

1. **Recolección de Datos**: Los sensores miden los parámetros ambientales y envían los datos al Arduino.
2. **Transmisión a Raspberry Pi**: El Arduino transmite los datos a la Raspberry Pi donde está ejecutándose Node-RED.
3. **Publicación en Kafka**: Node-RED, mediante un script en Python, publica los datos en los topics de Kafka.
4. **Consumo y Procesamiento**: Los consumidores de Kafka en el CPD reciben los datos, los procesan y los preparan para el almacenamiento.
5. **Almacenamiento en HDFS**: Los datos procesados se almacenan en el HDFS, distribuidos entre el namenode y los cinco datanodes.

## Beneficios del Sistema

- **Monitoreo en Tiempo Real**: La configuración con Kafka permite que los datos sean transmitidos y procesados en tiempo real.
- **Escalabilidad**: El uso de Kafka y HDFS asegura que el sistema puede escalar según las necesidades, tanto en términos de datos como de procesamiento.
- **Alta Disponibilidad**: La configuración de HDFS con múltiples datanodes asegura que los datos están disponibles incluso si algunos nodos fallan.
- **Flexibilidad en el Procesamiento**: Los consumidores de Kafka pueden ser adaptados para realizar distintos tipos de procesamiento según las necesidades específicas del proyecto.

---

Puedes usar esta estructura para crear un README en tu repositorio de GitHub, proporcionando una visión clara y detallada del sistema y sus componentes.
