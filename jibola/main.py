import first_example


if __name__ == "__main__":
    next_of_kin=[]
    next_of_kin1=first_example.create_next_of_kin("quin","ajohne","07062783014","female","wife")
    next_of_kin.append(next_of_kin1)
    first_example.register_native_to_cohort("segun", "john","male","08024355419","sleepyjohn@gmail.com",next_of_kin)
    print(first_example.cohort_eight[0].next_of_kin[0].first_name)
    