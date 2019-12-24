def more_stops(subtitles_text):
    """
    define additional stop words
    :param subtitles_text: text
    :return: cleaned text
    """
    custom_stop_words = ["i'm", "know", "get", "i've", "'", "he's", "come", "gonna", "going", "would", "i'll"
        , "back", "take", "that's", "said", "a", "can't", "good", "â", "let's", "there's"
        , "day", "right", "well", "we're", "one", "think", "go", "could", "little", "got", "us", "okay"
        , "hey", "tell", "sir", "like", "yeah", "man", "oh", "want", "need", "see", "yes", "really", "ok"
        , "men", "cannot", "must", "they're", "we'll", "way", "time", "what's", "make", "everything"
        , "new", "something", "much"]
    my_text = [w for w in subtitles_text if not w in custom_stop_words]
    return my_text


parent_folder = "\movies"
