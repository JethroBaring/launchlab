import openai from './openaiConfig';
import { Questions } from '.';

const generateMeta = async (
	trl1: string,
	trl2: string,
	trl3: string,
	mrl1: string,
	mrl2: string,
	mrl3: string,
	rrl1: string,
	rrl2: string,
	rrl3: string,
	arl1: string,
	arl2: string,
	arl3: string,
	orl1: string,
	orl2: string,
	orl3: string,
	irl1: string,
	irl2: string,
	irl3: string
) => {
	const description = await openai.chat.completions.create({
		model: 'gpt-3.5-turbo',
		messages: [
			{
				role: 'user',
				content: `
        Response in JSON format following the example:
        each question must be scored from 1-5
        Sample response:
        {
          "trl":"1,3,2",
          "mrl":"3,2,1",
          "rrl":"3,2,1",
          "arl":"3,2,1",
          "orl":"3,2,1",
          "irl":"3,2,1",
        }	
        
        Scoring Instructions:												
                                
        Each question should be rated on a scale from 1 (Very Poor) to 5 (Excellent), based on the startup’s response.												
        The scores for each readiness level are summed up to give a total score for that level.												
        The total scores from all readiness levels are then combined to give an overall readiness score.												
                                
        Individual Question Scoring:												
          1 (Very Poor): The response indicates a significant lack of readiness in this aspect.											
          2 (Poor): The response shows below-minimum readiness with substantial improvement needed.											
          3 (Fair): The response meets the basic minimum requirements for readiness.											
          4 (Good): The response indicates above-minimum readiness with strong potential.											
          5 (Excellent): The response demonstrates exceptional readiness in this aspect.
          
        Technology Readiness Level Questions
          1.${Questions[0].Technology?.[0]}
            Response: ${trl1}
          2. ${Questions[0].Technology?.[1]}
            Response: ${trl2}
          3.${Questions[0].Technology?.[2]}
            Response: ${trl3}
        Market Readiness Level Questions
          1.${Questions[0].Market?.[0]}
            Response: ${mrl1}
          2. ${Questions[0].Market?.[1]}
            Response: ${mrl2}
          3.${Questions[0].Market?.[2]}
            Response: ${mrl3}
        Regulatory Readiness Level Questions
          1.${Questions[0].Regulatory?.[0]}
            Response: ${rrl1}
          2. ${Questions[0].Regulatory?.[1]}
            Response: ${rrl2}
          3.${Questions[0].Regulatory?.[2]}
            Response: ${rrl3}
        Acceptance Readiness Level Questions
          1.${Questions[0].Acceptance?.[0]}
            Response: ${arl1}
          2. ${Questions[0].Acceptance?.[1]}
            Response: ${arl2}
          3.${Questions[0].Acceptance?.[2]}
            Response: ${arl3}
        Organizational Readiness Level Questions
          1.${Questions[0].Organizational?.[0]}
            Response: ${orl1}
          2. ${Questions[0].Organizational?.[1]}
            Response: ${orl2}
          3.${Questions[0].Organizational?.[2]}
            Response: ${orl3}
        Investment Readiness Level Questions
          1.${Questions[0].Investment?.[0]}
            Response: ${irl1}
          2. ${Questions[0].Investment?.[1]}
            Response: ${irl2}
          3.${Questions[0].Investment?.[2]}
            Response: ${irl3}
          `
			}
		]
	});

	return description.choices[0].message.content;
};

export default generateMeta;
