"""This exercise talks about a program who collects data of people"""

def main_program_execution():
        """Main program execution"""

        list_of_people_size = []
        count_masculine = sum_of_masculine_heights = count_feminine = 0

        for person in range(15):
            try:
                name = str(input("Please, digit your name: ")).strip()
                gender = str(input("Please, digit your gender: [M/F] ")).strip().upper()[0]
                height = float(input("Please, digit your height(in meters size): ").strip().replace(",", "."))


                if gender == "F":
                    count_feminine += 1

                if gender == "M":
                    sum_of_masculine_heights += height
                    count_masculine += 1

                mean_height = sum_of_masculine_heights / count_masculine

                list_of_people_size.append(height)


                if count_feminine + count_masculine >= 3:
                    print("+=" * 25)

                    print(f"[ {max(list_of_people_size)}m ] --> The highest masculine height!")
                    print(f"[ {mean_height:.2f} ] --> The mean of masculine height!")
                    print(f"[ {count_feminine} ] --> The number of feminine persons!")

                    print("+=" * 25)
                    break


            except(ValueError, TypeError, IndexError):
                print("Error! Try typing a correct value again.")
                break

            except ZeroDivisionError:
                print("Error! You cannot divide by zero!")


if __name__ == "__main__":
    main_program_execution()
