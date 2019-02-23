"""WARNINGS TO SHARE
1. user names are not case sensitive, they must be spelled completely differently
2. comment files are case sensitive and the extension must be specified!"""

# import modules
import os


# TODO: MAKE SURE THE PATHS WORK ON WINDOWS!!!!!!!!!!!!!!!!
# define the DataManager class and its methods
class DataManager:

    # define class attributes
    # TODO: make this private
    user_profiles = []
    base_dir = os.path.dirname(os.path.realpath(__file__))

    # set base directory upon instantiation & import existing users
    def __init__(self):
        os.chdir(self.base_dir)
        self.import_users()

    # clear user profiles attribute
    # TODO: make this private
    def clear_users(self):
        self.user_profiles.clear()

    # generate user data txt file
    # TODO: make this more efficient (FUTURE RELEASE)
    def gen_profile_settings(self):
        try:
            os.chdir('users/')
            with open('user_data.txt', 'w+') as user_data:
                user_data.close()
            os.chdir(self.base_dir)

        except FileNotFoundError:
            with open('user_data.txt', 'w+') as user_data:
                user_data.close()
            os.chdir(self.base_dir)

    # delete all user profile settings from the text file
    def delete_all_profiles(self):

        # change directory and create an empty user data file
        os.chdir('users/')
        try:
            os.remove('user_data.txt')
            self.gen_profile_settings()

        #
        except FileNotFoundError:
            self.gen_profile_settings()

        # move back to the base directory and notify the user
        os.chdir(self.base_dir)
        return 'All user data was successfully cleared!'

    # delete a user profile from the text file
    def delete_profile(self, user):

        # set wd to the users folder
        os.chdir('users/')

        # open the user data file and delete the profile
        # read original lines in file
        with open('user_data.txt', 'r+') as user_data:

            # read lines and rewrite lines that don't match the user input
            lines = user_data.readlines()
        user_data.close()

        # delete original user data file and write a new data file with the modified settings
        os.remove('user_data.txt')
        with open('user_data.txt', 'w+') as user_data:
            [user_data.write(line) for line in lines if user.lower() not in line]
        user_data.close()

        # return to base dir
        os.chdir(self.base_dir)

        # success message
        return 'Profile for user "' + user + '" successfully deleted!'

    # TODO: make a method for missing user profile file handling (FUTURE FEATURE)

    # import a user's comments
    # TODO: make this private
    def import_comments(self, user, file):

        # set wd to the data folder
        # TODO: test if this works when moving the project's folder
        os.chdir('comments/')

        # read comment file and read over blank
        with open(file) as comment_file:
            comment_lines = [line.strip() for line in comment_file.readlines() if line.strip()]
        comment_file.close()

        # append user & comments to comments attribute
        entry = {'user': user,
                 'comments': comment_lines}
        self.user_profiles.append(entry)

        # reset working directory to base directory
        os.chdir(self.base_dir)

    # create a user
    def create_user(self, user, file):

        # move to users directory
        os.chdir('users/')

        # get a list of all existing user names if there's a user data file
        # TODO: put this into a method
        try:
            with open('user_data.txt', 'r') as user_data:

                # import raw data and skip empty lines (needed to check for duplicates)
                user_names = [name.lower()[:name.find(' - ')] for name in
                              [line.strip() for line in user_data.readlines() if line.strip()]]

            # close file
            user_data.close()

        # create a user data file if it doesn't exist and create an empty list of user names
        # TODO: put this into a method
        except FileNotFoundError:
            with open('user_data.txt', 'w+') as user_data:
                user_data.close()
            user_names = []

        # write user to user_data file if name doesn't exist and the text file exists
        # make sure text file exists
        # TODO: this can probably be more efficient (FUTURE RELEASE)
        try:
            os.chdir('../comments/')
            with open(file, 'r') as comment_file:
                comment_file.close()
            os.chdir('../users/')

        # notify the user that the text file doesn't exist
        except FileNotFoundError:
            return "The text file you specified doesn't exist!"

        # write user data if user's name doesn't already exist in the user data file
        if user in user_names:
            return 'A user with that name already exists, please use a different name!'

        # write user data
        else:
            with open('user_data.txt', 'a') as user_data:
                user_data.write(user.lower() + ' - ' + file + '\n')
            user_data.close()

            # reset working directory to base directory
            os.chdir(self.base_dir)

            # import users again
            self.clear_users()
            self.import_users()

            # success message
            return 'User successfully added!'

    # import user data
    def import_users(self):

        # clear profiles to avoid duplicates
        self.clear_users()

        # change directory to user folder
        os.chdir('users/')

        # create a list of arguments to supply for importing data
        with open('user_data.txt', 'r') as user_data:

            # import raw data and skip empty lines
            raw_data = [line.strip() for line in user_data.readlines() if line.strip()]

            # clean data and create a list of import arguments
            import_arguments = []
            for line in raw_data:

                # remove newlines and unpack string into arguments
                user, file = line.split(' - ')

                # append arguments to list
                entry = [user, file]
                import_arguments.append(entry)

        # close the file
        user_data.close()

        # switch to base directory
        os.chdir(self.base_dir)

        # better version of above code
        for item in import_arguments:

            # define import arguments
            user, file = item

            # import
            self.import_comments(user, file)

        # reset working directory to base directory
        os.chdir(self.base_dir)

    # print users and associated text files
    # TODO: this works on my console but the formatting is messed up on Discord (INVESTIGATE, UPDATE)
    def print_users(self):
        # TODO: bug, make the column headers dynamic!
        # move to the users directory
        os.chdir('users/')

        # print the users if the user data file exists
        try:
            # read all lines from the user data file
            with open('user_data.txt', 'r') as user_data:
                comment_lines = [line.strip() for line in user_data.readlines() if line.strip()]
            user_data.close()

            # check if print_list is empty
            # TODO: make this a listcomp (FUTURE RELEASE)
            print_list = []
            if comment_lines:
                # print users' names and associated text file
                for line in comment_lines:
                    # unpack variables to print
                    user, file = line.split(' - ')

                    # append variables to the print list
                    print_list.append([user, file])

            # move back to the base directory
            os.chdir(self.base_dir)

            # create a message file to return to the user\
            msg = ''

            # print the column names w/ dynamic spacing
            try:
                user_space = ' ' * (len(max([sublist[0] for sublist in print_list], key=len)) - 1)
                file_space = ' ' * (len(max([sublist[1] for sublist in print_list], key=len)) - 1)
                msg += ('User:' + user_space + 'File:' + file_space + '\n')

            # handle errors with the max() function (results from an empty list
            except ValueError:
                pass

            # print all the users' names and associated text files
            if print_list:
                for entry in print_list:

                    # unpack variables
                    user, file = entry

                    # calculate divider spaces
                    divider = ' ' * (len(max([sublist[0] for sublist in print_list], key=len)) - len(user) + 4)

                    # print the variables w/ dynamic spacing
                    msg += (user + divider + file + '\n')

            # unless there is no user data
            else:
                msg = 'No user settings found!'

            # return the message to the user
            return msg

        # create a user data file if it doesn't exist
        # TODO: put this into a method (FUTURE)
        except FileNotFoundError:

            # create the file and notify the user
            with open('user_data.txt', 'w+') as user_data:
                user_data.close()

            # move back to the base directory
            os.chdir(self.base_dir)

            # warning message
            return "User data file didn't exist. Please try again."


# test the class (SOLELY FOR DEBUGGING, EDIT AS YOU PLEASE)
if __name__ == '__main__':

    # create a data manager
    dm = DataManager()

    # break
    print('BREAK')

    hm = dm.print_users()
    print(hm)
