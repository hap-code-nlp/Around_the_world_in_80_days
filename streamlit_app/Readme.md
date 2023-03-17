# Around_the_world_in_80_days - Streamlit Application

## Local Setup

1. Create a virtual environment

   ```bash
   python3 -m venv <ENV_NAME>
   ```

2. Install all the dependencies

   ```bash
   pip3 install -r requirements.txt
   ```

3. Install `en_core_web_lg` using the following command (OPTIONAL)

```bash
   python3 -m spacy download en_core_web_lg
```

4. Run `main.py` to generate all the dataset files.

   ```bash
   python3 main.py
   ```

5. Finally, Run `app.py` to execute your streamlit application.

   ```bash
   streamlit run app.py
   ```
