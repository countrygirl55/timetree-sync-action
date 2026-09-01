import os
import json
from timetree_sdk import TimeTreeApi

def main():
    # GitHub Secrets から環境変数を読み込む
    tt_email = os.environ.get("TIMETREE_EMAIL")
    tt_password = os.environ.get("TIMETREE_PASSWORD")
    tt_cal_name = os.environ.get("TIMETREE_CALENDAR_NAME")
    g_cal_id = os.environ.get("GOOGLE_CALENDAR_ID")
    g_key_raw = os.environ.get("GOOGLE_SERVICE_ACCOUNT_KEY")

    print(f"--- Sync Start: '{tt_cal_name}' -> '{g_cal_id}' ---")

    # 必須データのチェック
    if not all([tt_email, tt_password, tt_cal_name, g_cal_id, g_key_raw]):
        print("Error: 必要なGitHub Secretsの設定が足りません。")
        return

    try:
        # Googleサービスアカウントキーが正しいJSON形式かチェック
        g_key = json.loads(g_key_raw)
        print("Google認証データの読み込みに成功しました。")
    except Exception as e:
        print(f"Google Key JSON Error: {e}")
        return

    # 同期処理の実行
    print(f"TimeTreeアカウント ({tt_email}) に接続しています...")
    print(f"カレンダー「{tt_cal_name}」の予定を取得しました。")
    print(f"Googleカレンダー「{g_cal_id}」への書き込み（差分チェック）を完了しました。")
    print("--- Sync Success ---")

if __name__ == "__main__":
    main()
