name: Scrape Prices Daily

on:
  schedule:
    - cron: '0 8 * * *' # Hər gün saat 08:00-da işə düşür
  workflow_dispatch: # Əl ilə işə salmaq üçün düymə

jobs:
  build:
    runs-on: ubuntu-latest
    permissions:
      contents: write # İcazələri açırıq
      id-token: write
    steps:
      - uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.10'

      - name: Run Scraper
        run: python scrapers/scraper.py

      - name: Commit and push changes
        run: |
          git config --global user.name "github-actions[bot]"
          git config --global user.email "41898282+github-actions[bot]@users.noreply.github.com"
          git remote set-url origin https://x-access-token:${{ secrets.GITHUB_TOKEN }}@github.com/${{ github.repository }}
          git add data/prices.json
          
          # Dəyişiklikləri yoxlayıb commit və push edir
          if [ -n "$(git status --porcelain)" ]; then
            git commit -m "Avtomatik yenilənmiş qiymətlər"
            git push origin HEAD
          else
            echo "Heç bir dəyişiklik yoxdur."
          fi
