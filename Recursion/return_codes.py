# def all_codes(number):
#     """
#     :param: number - input integer
#     Return - list() of all codes possible for this number
#     TODO: complete this method and return a list with all possible codes for the input number
#     """
#     #This code should be away from the recursion part make another code
#     numbers = [i for i in range(1,27)]
#     letters = [l for l in 'abcdefghijklmnopqrstuvwxyz']
#     code_dict = dict(zip(numbers,letters))


#     s = ""
#     s = str(number)

#     #Defining the base case
#     if number == 0:
#         return

#     # rest = slice(len(s)+1,1)
#     if s[-1] != "":
#         all_codes(int(s[-1]))
#     else:#base_case
#         all_codes(0)

#     # return code_dict[number]

# all_codes(123)

###################Udacity solution########################################
def get_alphabet(number):
    """
    Helper function to get ascii character
    """
    return chr(number+96)


def all_codes(number):
    if number == 0:
        return [""]
 # calculation for two right-most digits e.g. if number = 1123, this calculation is meant for 23
    remainder = number%100
    output_100 = list()



    if remainder <=26 and number>9:
        # get all codes for the remaining number
        output_100 = all_codes(number// 100)
        alphabet = get_alphabet(remainder)

        for index,element in enumerate(output_100):
            output_100[index] = element + alphabet


     # calculation for right-most digit e.g. if number = 1123, this calculation is meant for 3
    remainder = number % 10
     # get all codes for the remaining number
    output_10 = all_codes(number//10)
    alphabet = get_alphabet(remainder)

    for index,element in enumerate(output_10):
            output_10[index] = element + alphabet

    output = list()
    output.extend(output_100)
    output.extend(output_10)

    return output

all_codes(1145)


