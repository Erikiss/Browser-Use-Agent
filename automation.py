import os
import sys
from browser_use_sdk import BrowserUse

def get_api_key() -> str:
    # GitHub Secret-Name, den du genannt hast
    key = os.getenv("BrowserUse_API")

    # Optionaler Fallback, falls du im Workflow lieber auf einen Standard-ENV-Namen mappst
    if not key:
        key = os.getenv("BROWSER_USE_API_KEY")

    if not key:
        print(
            "❌ Kein API-Key gefunden.\n"
            "Erwartet ENV 'BrowserUse_API' (oder optional 'BROWSER_USE_API_KEY').\n"
            "➡️ In GitHub Actions musst du das Secret in eine ENV-Variable setzen.",
            file=sys.stderr,
        )
        sys.exit(1)

    return key


def main() -> None:
    api_key = get_api_key()
    client = BrowserUse(api_key=api_key)

    task = client.tasks.create_task(
        task="Go to browser-use.com/changelog and summarize the latest updates."
    )

    result = task.complete()
    print(result.output)


if __name__ == "__main__":
    main()
