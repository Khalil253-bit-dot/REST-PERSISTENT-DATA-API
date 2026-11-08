# What I learned

I learned a very unexpected lesson from this assignment. When I tried to use the curl statements in the lesson to test my code,
I received a very long error message. I put the error into ChatGPT hoping to get some insight on what to fix, but it told
me that I coded everything correctly and that I  should hard-code a JSON file to feed into the program. A prompt refinement did
not help either, even though I put a screenshot of error into ChatGPT.

When I asked Gemini, though, it told me that the t_dict function was mostly likely outside of the ClinicalData class.
This turned out to be the exact issue. I learned that some AIs are better at certain tasks than others, and
one may be able to come up with a solution that another one either can't or won't without substantial refinement.

To complete the assignment, I added race, weight, and pre-existing conditions fields to the models.py file. VSCode then
auto suggested to correct syntax for adding the necessary code in the other files.
