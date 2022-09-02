import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
from AD_speech_features import *

##from AD_speech_features import AdjectiveFrequency
##from AD_speech_features import AdjectiveTypeFrequency
##from AD_speech_features import AdpositionFrequency
##from AD_speech_features import AdverbFrequency
##from AD_speech_features import AdverbTypeFrequency
##from AD_speech_features import AuxiliaryFrequency
##from AD_speech_features import BigramRepetitionFrequency
##from AD_speech_features import ConjunctionFrequency
##from AD_speech_features import DeterminerFrequency
##from AD_speech_features import FillerFrequency
##from AD_speech_features import FrequentVerbRatio
##from AD_speech_features import HapaxLegomenaFrequency
##from AD_speech_features import InflectedVerbRatio
##from AD_speech_features import NounFrequency
##from AD_speech_features import NounTypeFrequency
##from AD_speech_features import PronounFrequency
##from AD_speech_features import QuantityWordsFrequency
##from AD_speech_features import WordsUsedOnceOrTwice
##from AD_speech_features import RepeatedOpenClassWordsFrequency
##from AD_speech_features import RepeatedTotalOpenClassRatio
##from AD_speech_features import SichelS
##from AD_speech_features import TTR
##from AD_speech_features import UniAndBigramRepetitions
##from AD_speech_features import UnigramRepetitions
##from AD_speech_features import VerbFrequency
##from AD_speech_features import VerbTypeFrequency
##from AD_speech_features import OpenClosedRatio
##from AD_speech_features import NounPronounRatio
##from AD_speech_features import Honore
##from AD_speech_features import BrunetIndex
##from AD_speech_features import AverageWordLength
##from AD_speech_features import AverageWordFrequency
##from AD_speech_features import PastVerbRatio
##from AD_speech_features import IndefiniteNounRatio
##from AD_speech_features import GetAuxRatio
##from AD_speech_features import BeAuxRatio
##from AD_speech_features import BeGetRatio
##
##adjective_frequency = AdjectiveFrequency
##adjective_type_frequency = AdjectiveTypeFrequency
##adposition_frequency = AdpositionFrequency
##adverb_frequency = AdverbFrequency
##adverb_type_frequency = AdverbTypeFrequency

with open("/Users/ullapetti/AD_speech_features/data/full/001-03.txt", "r") as file:
        text = file.read()
        doc1 = nlp(text)


print(AdjectiveFrequency.adjective_freq(doc1))
print(AdjectiveTypeFrequency.adjective_type_freq(doc1))
print(AdpositionFrequency.adposition_freq(doc1))
print(AdverbFrequency.adverb_freq(doc1))
print(AdverbTypeFrequency.adverb_type_freq(doc1))
print(AuxiliaryFrequency.auxiliary_freq(doc1))
print(BigramRepetitionFrequency.bigram_rep_freq(doc1))
print(ConjunctionFrequency.conjunction_freq(doc1))
print(DeterminerFrequency.determiner_freq(doc1))
print(FillerFrequency.filler_freq(doc1))
print(FrequentVerbRatio.frequent_verb_ratio(doc1))
print(HapaxLegomenaFrequency.hapax_legomena_freq(doc1))
print(InflectedVerbRatio.inflected_verb_ratio(doc1))
print(NounFrequency.noun_freq(doc1))
print(NounTypeFrequency.noun_type_freq(doc1))
print(PronounFrequency.pronoun_freq(doc1))
print(WordsUsedOnceOrTwice.once_twice_freq(doc1))
print(RepeatedTotalOpenClassRatio.repeated_open_ratio(doc1))
print(SichelS.sichel_S(doc1))
print(TTR.TTR(doc1))
print(UniAndBigramRepetitions.unibi_reps(doc1))
print(UnigramRepetitions.uni_reps(doc1))
print(VerbFrequency.verb_freq(doc1))
print(VerbTypeFrequency.verb_type_freq(doc1))
print(OpenClosedRatio.open_closed_ratio(doc1))
print(NounPronounRatio.noun_pronoun_ratio(doc1))
print(Honore.honore(doc1))
print(BrunetIndex.brunet_index(doc1))
print(AverageWordLength.average_word_length(doc1))
print(AverageWordFrequency.average_word_frequency(doc1))
print(PastVerbRatio.past_verb_ratio(doc1))
print(IndefiniteNounRatio.indefinite_noun_ratio(doc1))
print(GetAuxRatio.get_aux_ratio(doc1))
print(BeAuxRatio.be_aux_ratio(doc1))
print(BeGetRatio.be_get_ratio(doc1))


