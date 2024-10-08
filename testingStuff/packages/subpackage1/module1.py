# module 1 in subpackage1

# 11 fun facts about Python
def pythonFunfact(i):
    """
    ### Returns a funfact about Python

    Args:
        `i`(int): an integer between 0 and 10

    Returns:
        `String`: the i-th funfact
    """

    funFacts = ["It was created As A Hobby Project",
                "It does Not Require A Compiler",
                "Python Has Variants",
                "It Is Older Than Java",
                "It was named After A Tv Show",
                "Python Is Similar To English",
                "Python Overtook French",
                "Python Follows Chain Comparison",
                "Python Is A Multipurpose Language",
                "Python is open source",
                "You Can Define Infinite Values"]
    return f"One funfact about python is, {funFacts[i]}"