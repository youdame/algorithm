def solution(babbling):
    발음 = ["aya", "ye", "woo", "ma"]
    count = 0
    
    for word in babbling:
        i = 0
        prev = ""
        while i < len(word):
            for sound in 발음:
                if word.startswith(sound, i) and sound != prev:
                    prev = sound
                    i += len(sound)
                    break
            else:

                break
        else:

            count += 1

    return count 