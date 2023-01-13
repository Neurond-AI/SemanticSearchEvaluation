# Semantic Search Evaluation
#### Evaluation metric for a semantic search system:
- Take a sample of questions from the test set.
- Consider the pool of top answers for each question.
- Consider a meta-scoring system of the following scheme: if the top answer is the right answer, then give it a 1; if the top answer is not correct but the right answer is present in the set of top answers returned by the model, then give it a number between 0 and 1 (You can set the rule for this); if the answer is not anywhere in the set of answers, then give it 0.
- Doing this for all the questions in the sample will give a score for each question.
- Sum up all the score for the smart search system, and divide with the total number of questions in the sample.
- Do all the above steps with top-6, top-8 and top-10 answers for each question and then multiple them together to get the final results.

#### The query.xlsx and the data.xlsx file are the sample data for queries and results of queries which is indexed in ID column. They are manually labelled.

#### The json files in the input folder are the output of different semantic search systems.
