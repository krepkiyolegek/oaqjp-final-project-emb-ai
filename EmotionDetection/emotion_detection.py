import requests
import json

def emotion_detector(text_to_analyse):
    # 1. Указываем адрес (URL) ИИ-модели Watson
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # 2. Формируем словарь с текстом так, как этого требует Watson
    myobj = { "raw_document": { "text": text_to_analyse } }
    
    # 3. Указываем заголовок (какую именно модель ИИ мы хотим использовать)
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # Отправляем POST-запрос
    response = requests.post(url, json=myobj, headers=header)

    # Преобразуем текст в словарь
    formatted_response = json.loads(response.text)
    
    # Извлекаем эмоции. 
    # Если посмотреть на терминал, наши данные лежат тут: 'emotionPredictions' -> первый элемент [0] -> 'emotion'
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    anger_score = emotions['anger']
    disgust_score = emotions['disgust']
    fear_score = emotions['fear']
    joy_score = emotions['joy']
    sadness_score = emotions['sadness']
    
    # Находим доминирующую эмоцию (ту, у которой самый высокий балл)
    dominant_emotion = max(emotions, key=emotions.get)
    
    # Формируем итоговый вывод
    result = {
        'anger': anger_score,
        'disgust': disgust_score,
        'fear': fear_score,
        'joy': joy_score,
        'sadness': sadness_score,
        'dominant_emotion': dominant_emotion
    }
    
    return result