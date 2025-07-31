# Mega Millions Predictor

This project predicts the Mega Ball number for the Mega Millions lottery using a simple neural network model. A Streamlit web app lets you pick five white ball numbers and shows the predicted Mega Ball along with the probability distribution for all numbers.

## Requirements
Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Running the app
Execute the Streamlit application:

```bash
streamlit run app.py
```

The app will load the pre-trained model `megaball_model.keras` and display an interface where you can select five white balls and see the predicted Mega Ball.

## Dataset
`Lottery_Mega_Millions_Winning_Numbers.csv` contains historical winning numbers used to train the model. It has 2419 rows.

## License
This project is released under the MIT License. See [LICENSE](LICENSE) for details.
