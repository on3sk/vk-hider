#!/usr/bin/env python3
import requests

# Кто будет видеть ваш "Онлайн".  По умолчанию - Только я
privat_value = "only_me" # Приватности [only_me] (только я), [all] (все), [friends] (друзья)

# Смотрим токен ===> https://oauth.vk.com/authorize?client_id=6146827&redirect_uri=https://oauth.vk.com/blank.html&display=page&response_type=token&revoke=1
token = "XxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxXxX"


headers = {
    'Connection': 'keep-alive',
    'Content-Type': 'text/html; charset=utf-8',
    'User-Agent': 'VKAndroidApp/1.777-999 (Android 2000; SDK 3572; script; 1; ru; 18x8000)',
    'Cache-control': 'no-store',
    'X-Frame-Options': 'SAMEORIGIN',
    'Content-Encoding': 'gzip',
    'Strict-Transport-Security': 'max-age=15768000'
}
r = requests.get("https://api.vk.me/method/account.setPrivacy?v=5.109&key=online&value=" + privat_value + "&access_token=" + token, headers=headers)
print("[+] Приватность успешно изменена на ==> " + privat_value + " <== [+]")
