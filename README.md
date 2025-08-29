
# BFHL API (Flask)

## How to Run Locally
1. Install Python >=3.8.
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Make sure `.env` exists with your identity.
4. Run the API:
```bash
python app.py
```
5. Test POST endpoint using curl or Postman:
```bash
curl -X POST http://127.0.0.1:5000/bfhl           -H "Content-Type: application/json"           -d '{"data":["a","1","334","4","R","$"]}'
```

## Deployment on Vercel
1. Push this repo to GitHub.
2. Import repo in Vercel.
3. Deploy — the endpoint `/bfhl` will be live.
