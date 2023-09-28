def capitalize(text: str) -> str:
    # Split the text into words
    words = text.split()
    
    # Capitalize each word and join them back into a string
    capitalized_words = [word.capitalize() for word in words]
    
    # Join the capitalized words with spaces to form the final string
    capitalized_text = ' '.join(capitalized_words)

    return capitalized_text
