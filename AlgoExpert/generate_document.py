class Solution:
    def generateDocument(self, characters, document):
        characterCounts = {}

        for character in characters:
            if character not in characterCounts:
                characterCounts[character] = 0
            characterCounts[character] += 1
        print(f"Characters: {characterCounts}")

        for character in document:
            if character not in characterCounts and characterCounts[character] == 0:
                return False
            characterCounts[character] -= 1
        print(f"Document: {characterCounts}")
        return True


S = Solution()
character = "Bste!hetsi ogEAxpelrt x "
document = "AlgoExpert is the Best!"
print(S.generateDocument(character, document))
