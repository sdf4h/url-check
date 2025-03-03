from transformers import pipeline

# Загружаем предварительно обученную модель анализа
# Предположим, что мы имеем классификатор, обученный на выявление фишинговых URL.
model_name = "your-phishing-url-model"  # Замените на вашу модель
classifier = pipeline("text-classification", model=model_name)

def analyze_url_with_model(url):
    # Прогоняем URL через модель, чтобы определить, подозрительный ли он
    print(f"Анализ URL с помощью нейросетевой модели: {url}")
    results = classifier(url)
    label = results[0]['label']
    score = results[0]['score']
    
    if label == "phishing":
        print(f"URL '{url}' определен как фишинговый с вероятностью {score:.2f}")
        log_suspicious_url(url)
    else:
        print(f"URL '{url}' безопасен с вероятностью {score:.2f}")

def log_suspicious_url(url):
    with open("suspicious_urls.log", "a") as log_file:
        log_file.write(f"{url}\n")

# Пример использования
analyze_url_with_model("http://example.com")
