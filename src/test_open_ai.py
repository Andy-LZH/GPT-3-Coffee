import os
import openai

if __name__ == "__main__":
    openai.api_key = os.getenv("OPENAI_API_KEY")
    
    region = input("Region: ")
    altitude = input("Altitude: ")
    variety = input("Variety: ")
    process = input("Processing Methods: ")
    prompt = "Region: " + region + ", Variety: " + variety + ", Altitude: " + altitude + ", Process: " + process + " -> "

    response = openai.Completion.create(
        model="davinci:ft-uc-davis-2022-05-23-20-13-52",
        prompt=prompt,
        max_tokens=64,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    print(response.choices[0].text)
