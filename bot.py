import os
from decouple import config
os.environ["OPENAI_API_KEY"] = config('OPENAI_API_KEY')
from decouple import config
from flask import Flask, render_template, request, jsonify
from werkzeug.middleware.proxy_fix import ProxyFix
from llama_index import VectorStoreIndex, SimpleDirectoryReader, ServiceContext, GPTVectorStoreIndex
from llama_index.llms import OpenAI

# Инициализируем Flask приложение
app = Flask(__name__)

# Добавляем прокси
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_port=1)

# Устанавливаем папку для статических файлов
app.static_folder = 'template/src'



# Загрузка документов
documents = SimpleDirectoryReader('Wiki/data').load_data()

# Изменим модель




llm = OpenAI(temperature=0, model='gpt-3.5-turbo')
service_context = ServiceContext.from_defaults(llm=llm)

index = VectorStoreIndex.from_documents(documents, service_context=service_context)

query_engine = index.as_query_engine()

# Определение маршрутов и обработчиков
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/query', methods=['POST'])
def handle_query():
    data = request.get_json()
    query = data.get('query')
    query = "Отвечай на русском: " + query

    if not query:
        return jsonify({"error": "No query provided"})

    response = query_engine.query(query)
    response_text = str(response)

    return jsonify({"response": response_text})

# Если файл запускается напрямую, а не импортируется
if __name__ == '__main__':
    # Запускаем приложение на хосте 0.0.0.0 (для доступа с внешних адресов)
    # и порту 5111
    app.run(host='0.0.0.0', port=5111)
