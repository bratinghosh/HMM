a1a=['.', 'ADJ', 'ADP', 'ADV', 'CONJ', 'DET', 'NOUN', 'NUM', 'PRON', 'PRT', 'VERB', 'X']
a1b=2649
a1c=12.059885650136557
a1d='function'
a2a=13
a2b=2.4630453700815003
a4a3=0.8689827219809665
a4b1=[('``', '.'), ('My', 'DET'), ('taste', 'NOUN'), ('is', 'VERB'), ('gaudy', 'ADV'), ('.', '.')]
a4b2=[('``', '.'), ('My', 'DET'), ('taste', 'NOUN'), ('is', 'VERB'), ('gaudy', 'ADJ'), ('.', '.')]
a4b3='Even though, the emission probability would suggest that gaudy should be ADJ, but the transition probability of VERB to ADV is much higher than that of VERB to ADJ in the model, thus making the biased POS tagger(after training on the corpus data) think gaudy is ADV.'
a4c=56.63057530953183
a4d=308.7122785474796
a4e=['DET', 'NOUN', 'ADP', 'DET', 'NOUN', 'VERB', 'ADV']
a5='The parser has 100% construction coverage, thus minimal attachment ambiguity. The POS tagger can be used to get the tags for each word, even the ones that have not been seen before. The tagger gives the best estimation of the tag, reducing POS ambiguity. Thus, tagger helps parser overcome the problem of unseen word tags and helps it to provide a parse for any well-formed sentence. Alone, the parser would do worse due to POS ambiguity, except for when tagger gets a wrong series of tags.'
a6='Total tags in Universal tagset is much less compared to Brown. Thus, there is a higher probability of seeing most of the constructions even with our small training corpus. This helps improve the accuracy of our model. If Brown tagset was used then we would encounter data sparsity by not seeing enough constructions to make good estimations using our model. Some tags might not be seen at all while training, making our model highly inaccurate. Larger training corpus would solve this problem.'
a3c=16.79319240474419
a3d='<s>'
