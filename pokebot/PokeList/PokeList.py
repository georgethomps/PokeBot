# import modules
from DataManager import DataManager

# import the DataManager
pldm = DataManager()


# define the PokeList class
class PokeList:

    # define class attributes
    poke_list = []

    # add a user to the list
    def load_user(self, user):

        # added error handling in case multiple users are added
        # TODO: might not require error handling, (TEST FOR THE FUTURE)
        try:
            # format user input to lowercase
            user.lower()

            # check to see if the user exists in the DataManager settings
            users = [profile['user'] for profile in pldm.user_profiles]
            if user not in users:
                return 'This user does not exist! Please create a user profile before proceeding.'

            # check to see if the user is already loaded
            elif user in self.poke_list:
                return 'This user is already in the poke list!'

            # add the user to the poke list
            else:
                self.poke_list.append(user)
                return 'User Successfully Loaded!'

        # print an error message if more than one user is added
        except TypeError:
            return 'You can only add one user at a time!'

    # remove a user from the list
    def unload_user(self, user):

        # form user input to lowercase
        user.lower()

        # check to see if the user is in the list
        if user not in self.poke_list:
            return 'This user was never loaded...'

        # remove the user from the list
        else:
            self.poke_list.remove(user)
            return 'User Successfully Unloaded!'

    # print the list
    def print_list(self):

        # set list header
        msg = 'Loaded Users:\n'

        # check to see if the list is empty
        if len(self.poke_list) != 0:

            # loop through all users on the poke list, append to the message and print
            msg += '\n'.join([user for user in self.poke_list])
            return msg

        # print an empty list
        else:
            return msg + 'NO USERS LOADED!'

    # clear the list
    def clear_list(self):
        self.poke_list.clear()
        return 'PokeList cleared!'
