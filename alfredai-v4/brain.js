import { Configuration, OpenAIApi } from "openai";
import readline from "readline";

import * as dotenv from 'dotenv' 
dotenv.config()

const configuration = new Configuration({
  organization: `${process.env.OPENAI_ORGANIZATION}`,
  apiKey: `${process.env.OPENAI_SECRET_KEY}`
  
});


const openai = new OpenAIApi(configuration);

const userInterface = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

userInterface.prompt();

userInterface.on("line", async (input) => {
  await openai
    .createChatCompletion({
      model: "gpt-3.5-turbo",
      messages: [
        {role: "system", content: "Your name is Alfred, You are a helpful and funny assistant."},
        { role: "user", content: input }, 
      ],
      temperature: 0.8,
      max_tokens: 60,
      top_p: 1.0,
      frequency_penalty: 0.0,
      presence_penalty: 0.0,
    })
    .then((res) => {
      console.log(res.data.choices[0].message.content);
      userInterface.prompt();
    })
    .catch((e) => {
      console.log(e);
    });
});
  
  
  
  
  
  
  