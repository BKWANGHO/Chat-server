from fastapi import FastAPI
import uvicorn

from example.bmi import BMI
from example.dice import Dice
from example.leap_year import LeapYear
from example.rps import RPS

app = FastAPI()

@app.get("/")
async def root():
    m = BMI()
    dice = Dice()
    rps = RPS()
    leap = LeapYear()
    bmi = BMI()

    rps.result()

    leap.is_leap_year()
    print(f'bmi : {bmi.getBMI()}')

    return {"dice" : dice.dice()}

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)