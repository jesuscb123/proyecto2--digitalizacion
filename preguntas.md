## Preguntas a responder

#### Ciclo de vida del dato (5b)
- **¿Cómo se gestionan los datos desde su generación hasta su eliminación en tu proyecto?**

Mi programa solo recopila como dato los textos copiados y que se almacenan en el portapeles. He realizado el proyecto de tal forma que se sobreescriba lo que copias, es decir, si has copiado un texto para traducirlo y, posteriormente, copias otro texto, el anterior se sistituye por el actual. 
Una vez que inicias el programa, y tienes algo copiado en el portapapeles, el software intentará enviarlo a la API de google translate para traducirlo automáticamente. Si lo que hay copiado, ya se ha traducido anteriormente mientras el programa estaba iniciado, no volverá a enviar ese dato a la api, sino que se quedará almacenada en una variable dentro del programa.
- **¿Qué estrategia sigues para garantizar la consistencia e integridad de los datos?**

Los datos en mi programa no pueden ser manipulados, debido a que solo se encarga de almacenar lo que tienes copiado en el portapepeles local, lo traduce y listo.
- **Si no trabajas con datos, ¿cómo podrías incluir una funcionalidad que los gestione de forma eficiente?**
Podriamos almacenarlos en ficheros o en bases de datos y encriptar esos datos para asegurar la integridad de los datos.

### Almacenamiento en la nube (5f):
- **Si tu software utiliza almacenamiento en la nube, ¿cómo garantizas la seguridad y disponibilidad de los datos?**

Mi software no utiliza almacenamiento en la nube.
- **¿Qué alternativas consideraste para almacenar datos y por qué elegiste tu solución actual?**

Almaceno los datos en una variable local dentro del programa, que se sustituye durante la ejecución si el usuario copia otro texto. 
Elegí esta solución debido a que los datos que se van a utilizar son solo textos que el usuario copia de forma local en su equipo para traducirlo, por ello no necesito almacenar datos en la nube.
- **Si no usas la nube, ¿cómo podrías integrarla en futuras versiones?**

Podría almacenar en la nube las frases, palabras o textos para que el usuario pueda consultarlo en cualquier momento, sin necesidad de volver a traducir texto que ya se haya traducido previamente.

### Seguridad y regulación (5i):
- **¿Qué medidas de seguridad implementaste para proteger los datos o procesos en tu proyecto?**


- **¿Qué normativas (e.g., GDPR) podrían afectar el uso de tu software y cómo las has tenido en cuenta?**

- **Si no implementaste medidas de seguridad, ¿qué riesgos potenciales identificas y cómo los abordarías en el futuro?**

