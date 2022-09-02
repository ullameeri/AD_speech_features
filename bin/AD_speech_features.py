
class AdjectiveFrequency:
    """
    Find adjective frequency in a txt file.
    Adjectives will be divided by total words
    in a given file.

    :param adjective_frequency: The text in nlp format
    :type adjective_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def adjective_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        adjectives = []      
        import spacy
        for token in doc:
            if token.pos_ == 'ADJ':
                adjectives.append(token)
        return len(adjectives) / len(tokens)


class AdjectiveTypeFrequency:
    """
    Find the frequency of adjective types
    (different adjectives) in a txt file.
    The number of different adjectives will
    be divided by total words in a given file.
    
    :param adjective__type_frequency: The text in nlp format
    :type adjective_type_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def adjective_type_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        adjectives = []
        import spacy
        for token in doc:
            if token.pos_ == 'ADJ':
                adjectives.append(str(token))
        adjective_types = set(adjectives)

        return len(adjective_types) / len(tokens)

class AdpositionFrequency:
    """
    Find adposition frequency in a txt file.
    Adpositions will be divided by total words in a given file.
    :param adposition_frequency: The text in nlp format
    :type adposition_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def adposition_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        adpositions = []
        import spacy
        for token in doc:
            if token.pos_ == 'ADP':
                adpositions.append(str(token))

        return len(adpositions) / len(tokens)


class AdverbFrequency:
    """
    Find adverb frequency in a txt file.
    Adverbs will be divided by total words in a given file.

    :param adverb_frequency: The text in nlp format
    :type adverb_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def adverb_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        adverbs = []      
        import spacy
        for token in doc:
            if token.pos_ == 'ADV':
                adverbs.append(token)
        return len(adverbs) / len(tokens)


class AdverbTypeFrequency:
    """
    Find the frequency of adverb types
    (different adverbs) in a txt file.
    The number of different adverbs will
    be divided by total words in a given file.
    
    :param adverb_type_frequency: The text in nlp format
    :type adverb_type_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def adverb_type_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        adverbs = []
        import spacy
        for token in doc:
            if token.pos_ == 'ADV':
                adverbs.append(str(token))
        adverb_types = set(adverbs)

        return len(adverb_types) / len(tokens)


class AuxiliaryFrequency:
    """
    Find auxiliary words frequency in a txt file.
    Auxiliary will be divided by total words in a given file.

    :param auxiliary_frequency: The text in nlp format
    :type auxiliary_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def auxiliary_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        auxiliaries = []      
        import spacy
        for token in doc:
            if token.pos_ == 'AUX':
                auxiliaries.append(token)
        return len(auxiliaries) / len(tokens)


class BigramRepetitionFrequency:

    """
    Find bigram repetition frequency in a txt file.
    Bigram repetitions (two identical consecutive
    tokens) will be divided by total words in a given file.

    :param bigram_rep_frequency: The text in nlp format
    :type bigram_rep_frequency: path to file
    """

    def __init__(doc):
        doc == doc


    def bigram_rep_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        bigram_reps = 0
        i = 1
        while i < len(tokens):
            if tokens[i-3] + tokens[i-2] == tokens[i-1] + tokens[i]:
                bigram_reps += 1
                i += 1
            else:
                i += 1

        if bigram_reps > 0:
            return bigram_reps / len(tokens)

        else:
            return ('no bigram reps')

class ConjunctionFrequency:
    """
    Find conjunction frequency in a txt file.
    Conjunctions will be divided by total words
    in a given file.
    
    :param conjunction_frequency: The text in nlp format
    :type conjunction_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def conjunction_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        conjunctions = []
        import spacy
        for token in doc:
            if token.pos_ == 'CCONJ':
                conjunctions.append(str(token))

        return len(conjunctions) / len(tokens)


class DeterminerFrequency:
    """
    Find determiner frequency in a txt file.
    Determiners will be divided by total words
    in a given file.

    :param determiner_frequency: The text in nlp format
    :type determiner_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def determiner_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        determiners = []      
        import spacy
        for token in doc:
            if token.pos_ == 'DET':
                determiners.append(token)
        return len(determiners) / len(tokens)

class FillerFrequency:

    """
    Find filler frequency in a txt file.
    Number of fillers will be divided by total
    words in a given file.

    :param filler_frequency: The text in nlp format
    :type filler_frequency: path to file
    """

    def __init__(doc):
        doc == doc


    def filler_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        fillers = []
        fillers_list = ["um", "uh", "em", "emn", "eh", "ah", "er", "hmm"]

        for token in doc:
            if str(token) in fillers_list:
                fillers.append(str(token))
            else:
                continue

        if len(fillers) > 0:
            return len(fillers) / len(tokens)
        else:
            return("no fillers")

class FrequentVerbRatio:

    """
    Find frequent verb : verb ratio in a txt file.
    Number of frequent verbs will be divided by
    total verbs in a given file.

    :param frequent_verb_ratio: The text in nlp format
    :type fequent_verb_ratio: path to file
    """

    def __init__(doc):
        doc == doc


    def frequent_verb_ratio(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        import spacy
        verbs = []
        frequent_verbs = []
        frequent_verbs_list = ['be', 'come',
                               'do', 'get',
                               'give', 'go',
                               'have', 'know',
                               'look', 'make',
                               'see', 'tell',
                               'think', 'want',
                               'ask', 'feel',
                               'find', 'forget',
                               'happen', 'hear',
                               'like', 'live',
                               'mean', 'meet',
                               'put', 'remember',
                               'run', 'say', 'seem',
                               'speak', 'suppose',
                               'take', 'use',
                               'walk', 'wonder']
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(str(token))
            if str(token) in frequent_verbs_list:
                frequent_verbs.append(str(token))

        return len(frequent_verbs) / len(verbs)


class HapaxLegomenaFrequency:

    """
    Find hapax legomena (words used once)
    frequency in a txt file.
    Number of hapax legomena will be divided
    by total words in a given file.

    :param hapax_legomena_freq: The text in nlp format
    :type hapax_legomena_freq: path to file
    """

    def __init__(doc):
        doc == doc


    def hapax_legomena_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        hapax = []
        for w in tokens:
            if tokens.count(w) == 1:
                hapax.append(str(w))

        return len(hapax) / len(tokens)

class InflectedVerbRatio:

    """
    Find inflected verb : verb ratio in a txt file.
    Number of inflected verbs will be divided by
    total verbs in a given file.

    :param inflected_verb_ratio: The text in nlp format
    :type inflected_verb_ratio: path to file
    """

    def __init__(doc):
        doc == doc


    def inflected_verb_ratio(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        import spacy
        verbs = []
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(str(token))
                
        inflected_verbs = []
        for token in verbs:
            if str(token).endswith('ing') or str(token).endswith('ed') or str(token).endswith('en') or str(token).endswith('s'):
                inflected_verbs.append(str(token))
        return len(inflected_verbs)/len(verbs)

        

class NounFrequency:
    """
    Find noun frequency in a txt file.
    Nouns will be divided by total words
    in a given file.

    :param noun_frequency: The text in nlp format
    :type noun_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def noun_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        nouns = []      
        import spacy
        for token in doc:
            if token.pos_ == 'NOUN':
                nouns.append(token)
        return len(nouns) / len(tokens)


class NounTypeFrequency:
    """
    Find the frequency of noun types
    (different nouns) in a txt file.
    The number of different nouns will
    be divided by total words in a given file.
    
    :param noun__type_frequency: The text in nlp format
    :type noun_type_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def noun_type_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        nouns = []
        import spacy
        for token in doc:
            if token.pos_ == 'NOUN':
                nouns.append(str(token))
        noun_types = set(nouns)

        return len(noun_types) / len(tokens)

class PronounFrequency:
    """
    Find pronoun frequency in a txt file.
    Pronouns will be divided by total words
    in a given file.

    :param pronoun_frequency: The text in nlp format
    :type pronoun_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def pronoun_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        pronouns = []      
        import spacy
        for token in doc:
            if token.pos_ == 'PRON':
                pronouns.append(token)
        return len(pronouns) / len(tokens)


class QuantityWordsFrequency:
    """
    Find the frequency of words indicating
    quantity in a txt file.
    Quantity words will be divided by total
    words in a given file.

    :param quantity_words_frequency: The text in nlp format
    :type quantity_words_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def quantity_words_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        quantity_words_used = []
        quantity_words_list = ["less", "few",
                               "fewer", "many",
                               "more", "much",
                               "amount", "quantity",
                               "all", "each",
                               "every", "lots",
                               "lot", "some",
                               "little", "plenty",
                               "most", "none",
                               "several", "both",
                               "half", "any",
                               "enough", "whole",
                               "sufficient", "couple",
                               "numerous", "single",
                               "hundreds", "too"]

        for token in doc:
            if token.pos_ == 'NUM':
                quantity_words_used.append(str(token))
                
            elif str(token) in quantity_words_list:
                quantity_words_used.append(str(token))
                
            else:
                continue

        return len(quantity_words_used)/len(tokens)
    

class WordsUsedOnceOrTwice:
    """
    Find the ratio of words used once or twice
    to total words in a txt file.
    Number of words used up to two times will
    be divided by total words in a given file.

    :param once_twice_freq: The text in nlp format
    :type once_twice_freq: path to file
    """

    def __init__(doc):
        doc == doc


    def once_twice_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        once_twice_used_words = []
        for w in tokens:
            if tokens.count(w) == 1 or tokens.count(w) == 2:
                once_twice_used_words.append(str(w))

        return len(once_twice_used_words)/len(tokens)


class RepeatedOpenClassWordsFrequency:
    """
    Find the number of repeated open class words
    in 10 consecutive open class words divided
    by total words in a txt file.
    Number of repeated open class words in 10
    consecutive open class words will be divided
    by total words in a given file.

    :param repeated_open_freq: The text in nlp format
    :type repeated_open_freq: path to file
    """
    def __init__(doc):
        doc == doc

    def repeated_open_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        open_class = []
        for token in doc:
            if (token.pos_ == 'VERB' or
                token.pos_ == 'PROPN'or
                token.pos_ == 'NOUN'or
                token.pos_ == "INTJ" or
                token.pos_ == "ADV" or
                token.pos_ == "ADJ"):
                open_class.append(str(token))

        repeated_open_class_words = 0
        i = -1
        for word in open_class:
            i += 1
            ten_open = open_class[i:i+9]
            if ten_open.count(word) > 1:
                repeated_open_class_words += 1

        return repeated_open_class_words / len(tokens)


class RepeatedTotalOpenClassRatio:
    """
    Find the ratio of repeated open class
    words in 10 consecutive open class words,
    and total open class words in a txt file.
    Number of repeated open class words in
    10 consecutive open class words will be
    divided by the total number of open class
    words in a given file.

    :param repeated_open_ratio: The text in nlp format
    :type repeated_open_ratio: path to file
    """
    def __init__(doc):
        doc == doc

    def repeated_open_ratio(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        open_class = []
        for token in doc:
            if (token.pos_ == 'VERB' or
                token.pos_ == 'PROPN' or
                token.pos_ == 'NOUN' or
                token.pos_ == "INTJ" or
                token.pos_ == "ADV" or
                token.pos_ == "ADJ"):
                open_class.append(str(token))

        repeated_open_class_words = 0
        i = -1
        for word in open_class:
            i += 1
            ten_open = open_class[i:i+9]
            if ten_open.count(word) > 1:
                repeated_open_class_words += 1

        return repeated_open_class_words / len(open_class)
    

class SichelS:
    """
    Find Sichel's S - the words used twice
    divided by total words in a txt file.
    Number of words used two times will be
    divided by total words in a given file.

    :param Sichel_S: The text in nlp format
    :type Sichel_S: path to file
    """

    
    def __init__(doc):
        doc == doc


    def sichel_S(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        words_used_twice = []
        for w in tokens:
            if tokens.count(w) == 2:
                words_used_twice.append(str(w))

        return len(words_used_twice)/len(tokens)

class TTR:
    """
    Find type:token ratio in a txt file.
    Number of different words used will be
    divided by total words in a given file.

    :param TTR: The text in nlp format
    :type TTR: path to file
    """

    def __init__(doc):
        doc == doc


    def TTR(doc):
        
        tokens = []
        for token in doc:
            tokens.append(str(token))

        types = set(tokens)

        return len(types)/len(tokens)

class UniAndBigramRepetitions:
    """
    Find the number of uni- and bigram
    consecutive repetitions divided by
    total words in a txt file.
    Number of times the same unigram or
    bigram appears next to each other
    (immidiate repetition / stutter) will
    be divided by total words in a given file.

    :param unibi_reps: The text in nlp format
    :type unibi_reps: path to file
    """
    
    def __init__(doc):
        doc == doc

    def unibi_reps(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))

        unigram_reps = []
        i = 1
        while i < len(tokens):
            if tokens[i-1] == tokens[i]:
                unigram_reps.append(tokens[i])
                i += 1
            else:
                i += 1


        bigram_reps = 0
        i = 1
        while i < len(tokens):
            if tokens[i-3] + tokens[i-2] == tokens[i-1] + tokens[i]:
                bigram_reps += 1
                i += 1
            else:
                i += 1
                

        if (len(unigram_reps) + bigram_reps) == 0:
            return("no uni+bigram reps")
        elif (len(unigram_reps) + bigram_reps) > 0:
            return (len(unigram_reps) + bigram_reps) / len(tokens)

        
        
class UnigramRepetitions:
    """
    Find the number of unigram repetitions divided
    by total words in a txt file.
    Number of times the same single words appear
    next to each other will be divided by total
    words in a given file.

    :param uni_reps: The text in nlp format
    :type uni_reps: path to file
    """

    def __init__(doc):
        doc == doc
        
    def uni_reps(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
    
        unigram_reps = []
        i = 1
        while i < len(tokens):
            if tokens[i-1] == tokens[i]:
                unigram_reps.append(tokens[i])
                i += 1
            else:
                i += 1

        if len(unigram_reps) > 0:
            return len(unigram_reps) / len(tokens)

        else:
            return('no unigram repetitions')

class VerbFrequency:
    """
    Find verb frequency in a txt file.
    Verbs will be divided by total words in a given file.

    :param verb_frequency: The text in nlp format
    :type verb_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def verb_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        verbs = []      
        import spacy
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(token)
                
        return len(verbs) / len(tokens)


class VerbTypeFrequency:
    """
    Find the frequency of verb types
    (different adjectives) in a txt file.
    The number of different verbs will be
    divided by total words in a given file.
    
    :param verb__type_frequency: The text in nlp format
    :type verb_type_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def verb_type_freq(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        verbs = []
        import spacy
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(str(token))
        verb_types = set(verbs)

        return len(verb_types) / len(tokens)
    

class OpenClosedRatio:
    """
    Find the ratio of open and closed class
    words in a txt file.
    The number open class words will be divided
    by the number of closed class words in a given file.
    
    :param open_closed_ratio: The text in nlp format
    :type open_closed_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def open_closed_ratio(doc):
        open_class = []
        closed_class = []
        import spacy
        for token in doc:
            if (token.pos_ == 'VERB' or
                token.pos_ == 'PROPN' or
                token.pos_ == 'NOUN' or
                token.pos_ == "INTJ" or
                token.pos_ == "ADV" or
                token.pos_ == "ADJ"):
                open_class.append(token)
                
            if (token.pos_ == 'ADP' or
                token.pos_ == 'AUX' or
                token.pos_ == 'CCONJ' or
                token.pos_ == 'DET' or
                token.pos_ == 'NUM' or
                token.pos_ == 'PART' or
                token.pos_ == 'PRON' or
                token.pos_ == 'SCONJ'):
                closed_class.append(token)
                
            else:
                continue
            
        if len(closed_class) == 0:
            return("no closed class words")
        else: 
            return len(open_class)/len(closed_class)



        

class NounPronounRatio:
    """
    Find noun:pronoun ratio in a txt file.
    Nouns will be divided by pronouns in a given file.

    :param noun_pronoun_ratio: The text in nlp format
    :type noun_pronoun_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def noun_pronoun_ratio(doc):
        import spacy
        nouns = []
        for token in doc:
            if token.pos_ == 'NOUN':
                nouns.append(token)
        pronouns = []      
        for token in doc:
            if token.pos_ == 'PRON':
                pronouns.append(token)
                
        return len(nouns) / len(pronouns)


class Honore:
    """
    Find Honore statistic in a txt file.
    Honore statistic measuring vocabulary
    richness will be calculated in a given file.
    The higher the number the more diverse the vocabulary.

    :param honore: The text in nlp format
    :type honore: path to file
    """

    def __init__(doc):
        doc == doc

    def honore(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        types = set(tokens)
        
        hapax = []
        for w in tokens:
            if tokens.count(w) == 1:
                hapax.append(str(w))

        N = len(tokens)
        U = len(types)
        Nuni = len(hapax)

        import math

        honore = 100 * math.log(N)/(1-Nuni/U)
        return honore


class BrunetIndex:
    """
    Find Brunet index in a txt file.
    Brunet index measuring vocabulary
    richness will be calculated in a given file.
    The lower the number the more diverse the vocabulary.

    :param brunet_index: The text in nlp format
    :type brunet_index: path to file
    """

    def __init__(doc):
        doc == doc

    def brunet_index(doc):
        tokens = []
        for token in doc:
            tokens.append(str(token))
        
        types = set(tokens)
        
        N = len(tokens)
        U = len(types)

        brunet_index = N**U**-0.165

        return brunet_index


class AverageWordLength:
    """
    Find average word length in a txt file.
    Average length of the word will be calculated
    in a given file.

    :param average_word_length: The text in nlp format
    :type average_word_length: path to file
    """

    def __init__(doc):
        doc == doc

    def average_word_length(doc):
        
        tokens = []
        for token in doc:
            tokens.append(str(token))
            
        word_len = []
        for word in tokens:
            word_len.append(len(word))

        from statistics import mean

        return mean(word_len)

class AverageWordFrequency:
    """
    Find average word frequency in a txt file.
    Average frequency of the words will be calculated
    in a given file.

    :param average_word_frequency: The text in nlp format
    :type average_word_frequency: path to file
    """

    def __init__(doc):
        doc == doc

    def average_word_frequency(doc):
        
        zipf_freqs = []
        from wordfreq import zipf_frequency
        for token in doc:
            zipf_freqs.append((float(zipf_frequency(str(token), 'en'))))

        from statistics import mean

        return mean(zipf_freqs)

            

class PastVerbRatio:
    """
    Find the ratio of past tense verbs and all
    verbs in a txt file.
    Past tense verbs will be divided by total
    verbs in a given file.

    :param past_verb_ratio: The text in nlp format
    :type past_verb_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def past_verb_ratio(doc):
        
        past_tense = []
        verbs = []
        import spacy
        for token in doc:
            if token.pos_ == 'VERB':
                verbs.append(token)
                    
        for token in verbs:
            if token.tag_ == 'VBD':
                past_tense.append(str(token))

        return len(past_tense)/len(verbs)


class IndefiniteNounRatio:
    """
    Find the ratio of indefinite nouns and
    total nouns in a txt file.
    Indefinite ouns will be divided by total
    nouns in a given file.

    :param indefinite_noun_ratio: The text in nlp format
    :type indefinite_noun_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def indefinite_noun_ratio(doc):

        import spacy

        nouns = [] 
        for token in doc:
            if token.pos_ == 'NOUN':
                nouns.append(token)

        indefinite_nouns = []
        indefinite_nouns_list = ['thing', 'things',
                                 'something', 'anything',
                                 'nothing']
        for token in doc:
            if str(token) in indefinite_nouns_list:
                indefinite_nouns.append(str(token))
            

        if len(indefinite_nouns) == 0:
            return ("no indefinite nouns")
        else:
            return len(indefinite_nouns) / len(nouns)
                

class GetAuxRatio:
    """
    Find the ratio of the word "get" and the
    auxiliary words in a txt file.
    Occurences of "get" will be divided by total
    auxiliaries in a given file.

    :param get_aux_ratio: The text in nlp format
    :type get_aux_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def get_aux_ratio(doc):
        
        import spacy
        
        get_auxiliaries = 0
        auxiliaries = 0
        
        for token in doc:
            if token.pos_ == 'AUX':
                 auxiliaries += 1
                 
            if (token.pos_ == "AUX" and
                str(token) == "get"):
                get_auxiliaries += 1
                
        if get_auxiliaries == 0:
            return ("no 'get' auxiliaries")
        
        if auxiliaries == 0:
            return ("no auxiliaries")
        
        else:
            return get_auxiliaries / auxiliaries
        

class BeAuxRatio:
    """
    Find the ratio of the word "be" and
    the auxiliary words in a txt file.
    Occurences of "be" will be divided
    by total auxiliaries in a given file.

    :param be_aux_ratio: The text in nlp format
    :type be_aux_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def be_aux_ratio(doc):

        import spacy
        
        be_auxiliaries = 0
        auxiliaries = 0
        
        for token in doc:
            if token.pos_ == 'AUX':
                 auxiliaries += 1
                 
            if (token.pos_ == "AUX" and
                str(token) == "be"):
                be_auxiliaries += 1
                
        if be_auxiliaries == 0:
            return ("no 'be' auxiliaries")
        
        if auxiliaries == 0:
            return ("no auxiliaries")
        
        else:
            return be_auxiliaries / auxiliaries


        
class BeGetRatio:
    """
    Find the ratio of the words "be" and
    "get" in a txt file.
    Occurences of "be" will be divided by
    occurences of "get" in a given file.

    :param be_get_ratio: The text in nlp format
    :type be_get_ratio: path to file
    """

    def __init__(doc):
        doc == doc

    def be_get_ratio(doc):
        
        import spacy
        
        be_auxiliaries = 0
        get_auxiliaries = 0
        
        for token in doc:
            if (token.pos_ == "AUX" and
                str(token) == "be"):
                be_auxiliaries += 1
                
            if (token.pos_ == "AUX" and
                str(token) == "get"):
                get_auxiliaries += 1
                
        if get_auxiliaries == 0:
            return ("no 'get' auxiliaries")
        
        if be_auxiliaries == 0:
            return ("no 'be' auxiliaries")
        
        else:
            return be_auxiliaries / get_auxiliaries
