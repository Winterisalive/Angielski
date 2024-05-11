import os
import win32gui

def clear_console():
    # Wyczyszczenie konsoli na platformie Windows
    os.system('cls')


# Definicje dla czasów gramatycznych Present Simple, Present Continuous, Present Perfect itd.

def present_simple_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Present Simple")
    print("2. Użycie -s w trzeciej osobie liczby pojedynczej")
    print("3. Określanie częstotliwości")
    print("4. 'to be' jako czasownik główny")
    print("0. Powrót do głównego menu")


def present_simple():
    clear_console()
    print("Present Simple jest bardzo prosty w tworzeniu. Potrzeba tylko czasownika w podstawowej formie i osoby wykonującej czynność.")
    print("Czas Present Simple składa się z następujących elementów:")
    print("podmiot + czasownik w formie podstawowej")
    print("Oto przykład:")
    print("I go to the cinema once a week. - Chodzę do kina raz w tygodniu.")
    input("Wciśnij Enter aby kontynuować...")


def present_simple_usage_s():
    clear_console()
    print("Użycie -s w trzeciej osobie liczby pojedynczej:")
    print("W czasie Present Simple, w trzeciej osobie liczby pojedynczej, do czasownika dodaje się końcówkę -s lub -es.")
    print("Oto przykłady:")
    print("He plays tennis every Sunday. - On gra w tenisa każdego niedzielnego.")
    print("She watches TV in the evening. - Ona ogląda telewizję wieczorami.")
    input("Wciśnij Enter aby kontynuować...")


def present_simple_frequency():
    clear_console()
    print("Określanie częstotliwości:")
    print("W czasie Present Simple, częstotliwość wydarzeń może być określana za pomocą słów takich jak:")
    print("always, usually, often, sometimes, rarely, seldom, never, every day/week/month/year, on Mondays/Sundays, etc.")
    print("Oto przykłady:")
    print("I usually drink coffee in the morning. - Zazwyczaj piję kawę rano.")
    print("They never go to bed early. - Oni nigdy nie kładą się wcześnie spać.")
    input("Wciśnij Enter aby kontynuować...")


def present_simple_to_be():
    clear_console()
    print("'to be' jako czasownik główny:")
    print("Czas Present Simple jest również używany do opisywania stałych sytuacji, faktów ogólnych, zawodów, lub do określania właściwości.")
    print("Oto przykłady:")
    print("She is a teacher. - Ona jest nauczycielką.")
    print("The Earth orbits around the Sun. - Ziemia krąży wokół Słońca.")
    input("Wciśnij Enter aby kontynuować...")


def present_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Present Continuous")
    print("2. Użycie Present Continuous")
    print("3. Czasowniki zakończone na -ing")
    print("0. Powrót do głównego menu")


def present_continuous():
    clear_console()
    print("Present Continuous opisuje czynności, które dzieją się w chwili obecnej.")
    print("Czas Present Continuous składa się z następujących elementów:")
    print("podmiot + to be (am/is/are) + czasownik zakończony na -ing")
    print("Oto przykład:")
    print("She is reading a book right now. - Ona teraz czyta książkę.")
    input("Wciśnij Enter aby kontynuować...")


def present_continuous_usage():
    clear_console()
    print("Użycie Present Continuous:")
    print("Czas Present Continuous stosujemy do czynności, które dzieją się w chwili obecnej, ale mogą też być zaplanowane na przyszłość.")
    print("Oto przykłady:")
    print("I am meeting my friend after work. - Spotykam się z przyjacielem po pracy.")
    print("They are not playing football today. - Oni dzisiaj nie grają w piłkę nożną.")
    input("Wciśnij Enter aby kontynuować...")


def present_continuous_verb_ing():
    clear_console()
    print("Czasowniki zakończone na -ing:")
    print("W czasie Present Continuous czasownik zawsze kończy się na -ing.")
    print("Oto przykłady:")
    print("She is reading a book. - Ona czyta książkę.")
    print("They are playing football. - Oni grają w piłkę nożną.")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Present Perfect")
    print("2. Użycie Present Perfect")
    print("3. Różnice między Present Perfect a Past Simple")
    print("0. Powrót do głównego menu")


def present_perfect():
    clear_console()
    print("Present Perfect opisuje czynności, które zdarzyły się w przeszłości i mają związek z teraźniejszością.")
    print("Czas Present Perfect składa się z następujących elementów:")
    print("podmiot + have/has + czasownik w formie trzeciej (czasownik regularny: -ed, czasownik nieregularny: 3. forma)")
    print("Oto przykład:")
    print("I have visited London many times. - Byłem w Londynie wiele razy.")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_usage():
    clear_console()
    print("Użycie Present Perfect:")
    print("Czas Present Perfect stosujemy do czynności, które rozpoczęły się w przeszłości i mają związek z teraźniejszością lub trwają do teraźniejszości.")
    print("Oto przykłady:")
    print("She has lived here for five years. - Ona mieszka tu od pięciu lat.")
    print("They have already finished their homework. - Oni już skończyli swoją pracę domową.")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_differences():
    clear_console()
    print("Różnice między Present Perfect a Past Simple:")
    print("Present Perfect używamy, gdy chcemy podkreślić związek przeszłości z teraźniejszością lub trwanie czynności do teraźniejszości.")
    print("Past Simple używamy, gdy chcemy opisać czynność, która zakończyła się w przeszłości i nie ma związku z teraźniejszością.")
    print("Oto przykłady:")
    print("Present Perfect: I have lost my keys. - Zgubiłem klucze i nie mogę ich teraz znaleźć.")
    print("Past Simple: I lost my keys yesterday. - Wczoraj zgubiłem klucze, ale teraz już je znalazłem.")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Present Perfect Continuous")
    print("2. Użycie czasu Present Perfect Continuous")
    print("3. Użycie modalnych czasowników z czasem Present Perfect Continuous")
    print("0. Powrót do głównego menu")


def present_perfect_continuous():
    clear_console()
    print("Present Perfect Continuous (Czas teraźniejszy doskonały ciągły) to czas używany, aby wskazać na kontynuującą się akcję, która rozpoczęła się w przeszłości i trwa nadal w chwili obecnej.")
    print("Czas Present Perfect Continuous składa się z następujących elementów:")
    print("podmiot + have/has been + czasownik z końcówką -ing")
    print("Oto przykład:")
    print("I have been reading this book for two hours. (Czytam tę książkę od dwóch godzin.)")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_continuous_usage():
    clear_console()
    print("Użycie czasu Present Perfect Continuous:")
    print("Present Perfect Continuous jest używany do wyrażania kontynuującej się akcji, która zaczęła się w przeszłości i trwa do chwili obecnej lub niedawno.")
    print("Oto przykłady:")
    print("- She has been studying English since she was a child. (Ona uczy się angielskiego od dziecka.)")
    print("- They have been working on this project since last year. (Oni pracują nad tym projektem od zeszłego roku.)")
    input("Wciśnij Enter aby kontynuować...")


def present_perfect_continuous_modal_verbs():
    clear_console()
    print("Użycie modalnych czasowników z czasem Present Perfect Continuous:")
    print("Modalne czasowniki, takie jak can, may, might, must, should, ought to, używane są w czasie Present Perfect Continuous, aby wyrazić możliwość, zobowiązanie, pozwolenie lub sugestię w odniesieniu do kontynuującej się akcji.")
    print("Oto przykłady:")
    print("- He may have been waiting for us at the airport. (On może na nas czekać na lotnisku.)")
    print("- You should have been paying more attention during the class. (Powinieneś był bardziej uważać podczas lekcji.)")
    input("Wciśnij Enter aby kontynuować...")


def past_simple_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Past Simple")
    print("2. Użycie Past Simple")
    print("3. Czasowniki regularne i nieregularne")
    print("0. Powrót do głównego menu")


def past_simple_usage():
    clear_console()
    print("Użycie Past Simple:")
    print("Czas Past Simple stosujemy do opisywania czynności, które wydarzyły się w określonym punkcie w przeszłości.")
    print("Oto przykłady:")
    print("I watched a movie last night. - Ostatniej nocy oglądałem film.")
    input("Wciśnij Enter aby kontynuować...")


def past_simple_regular_irregular():
    clear_console()
    print("Czasowniki regularne i nieregularne:")
    print("W czasie Past Simple, czasowniki regularne tworzą przeszłą formę przez dodanie -ed do podstawowej formy czasownika.")
    print("Czasowniki nieregularne mają własne formy przeszłe, które należy zapamiętać.")
    print("Oto przykłady:")
    print("Regularny: work -> worked, watch -> watched")
    print("Nieregularny: go -> went, eat -> ate")
    input("Wciśnij Enter aby kontynuować...")


def past_simple():
    clear_console()
    print("Past Simple opisuje czynności, które wydarzyły się w określonym punkcie w przeszłości.")
    print("Czas Past Simple składa się z następujących elementów:")
    print("podmiot + czasownik w formie przeszłej (czasownik regularny: -ed, czasownik nieregularny: 2. forma)")
    print("Oto przykład:")
    print("I watched a movie last night. - Ostatniej nocy oglądałem film.")
    input("Wciśnij Enter aby kontynuować...")


def past_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Past Continuous")
    print("2. Użycie Past Continuous")
    print("3. Czasowniki zakończone na -ing")
    print("0. Powrót do głównego menu")


def past_continuous():
    clear_console()
    print("Past Continuous opisuje czynności, które działy się w określonym punkcie w przeszłości.")
    print("Czas Past Continuous składa się z następujących elementów:")
    print("podmiot + was/were + czasownik zakończony na -ing")
    print("Oto przykład:")
    print("I was reading a book when you called. - Czytałem książkę, gdy do mnie dzwoniłeś.")
    input("Wciśnij Enter aby kontynuować...")


def past_continuous_usage():
    clear_console()
    print("Past Continuous Użycie:")
    print("Czasu past Continuous używamy do opisania czynności, które trwały lub miały miejsce w określonym momencie w przeszłości")
    print("Oto przykład:")
    print("I was studying when she called me. - Studiowałem, gdy zadzwoniła do mnie.")
    input("Wciśnij Enter aby kontynuować...")


def past_continuous_verb_ing():
    clear_console()
    print("Past Continuous Verb + -ing:")
    print("Czas przeszły ciągły tworzy się poprzez użycie czasu przeszłego „być” (was/were) i dodanie imiesłowu czasu teraźniejszego (podstawowa forma czasownika + -ing).")
    print("Oto przykład:")
    print("They were playing football when it started raining. - Oni grali w piłkę nożną, gdy zaczęło padać.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Past Perfect")
    print("2. Użycie Past Perfect")
    print("3. Różnice między Past Perfect a Past Simple")
    print("0. Powrót do głównego menu")


def past_perfect():
    clear_console()
    print("Past Perfect opisuje czynności, które wydarzyły się wcześniej w przeszłości, przed innymi czynnościami.")
    print("Czas Past Perfect składa się z następujących elementów:")
    print("podmiot + had + czasownik w trzeciej formie (czasownik regularny: -ed, czasownik nieregularny: 3. forma)")
    print("Oto przykład:")
    print("I had already eaten when she arrived. - Ja już zjadłem, gdy ona przybyła.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_usage():
    clear_console()
    print("Użycie Past Perfect:")
    print("Czas Past Perfect stosujemy, aby wyrazić, że jedno zdarzenie w przeszłości nastąpiło wcześniej niż inne.")
    print("Oto przykłady:")
    print("They had left before I arrived. - Oni odeszli, zanim ja przybyłem.")
    print("She had already finished her homework when he called. - Ona już skończyła pracę domową, gdy do niej zadzwonił.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_differences():
    clear_console()
    print("Różnice między Past Perfect a Past Simple:")
    print("Past Perfect używamy, aby podkreślić, że jedno zdarzenie w przeszłości nastąpiło wcześniej niż inne.")
    print("Past Simple opisuje zdarzenia, które wydarzyły się w określonym punkcie w przeszłości.")
    print("Oto przykłady:")
    print("Past Perfect: She had already left when I arrived. - Ona już wyszła, gdy ja przybyłem.")
    print("Past Simple: She left before I arrived. - Ona wyszła, zanim ja przybyłem.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Past Perfect Continuous")
    print("2. Użycie Past Perfect Continuous")
    print("3. Czasowniki zakończone na -ing")
    print("0. Powrót do głównego menu")


def past_perfect_continuous():
    clear_console()
    print("Past Perfect Continuous opisuje czynności, które rozpoczęły się w przeszłości i trwały do innego momentu w przeszłości.")
    print("Czas Past Perfect Continuous składa się z następujących elementów:")
    print("podmiot + had + been + czasownik zakończony na -ing")
    print("Oto przykład:")
    print("I had been waiting for two hours when the bus finally arrived. - Czekałem dwie godziny, gdy w końcu przyjechał autobus.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_continuous_usage():
    clear_console()
    print("Past Perfect Continuous Użycie:")
    print("Czasu Past Perfect Continuous używamy do opisania czynności, które trwały i miały miejsce przez pewien czas przed inną czynnością lub punktem w przeszłości.")
    print("Oto przykład:")
    print("I had been working for five hours when she arrived. - Pracowałem przez pięć godzin, gdy ona przyjechała.")
    input("Wciśnij Enter aby kontynuować...")


def past_perfect_continuous_modal_verbs():
    clear_console()
    print("Czasowniki modalne (will have been):")
    print("W czasie Past Perfect Continuous używamy will have been.")
    print("Oto przykłady:")
    print("By tomorrow, I will have been working here for five years. - Jutro będę pracował tutaj przez pięć lat.")
    input("Wciśnij Enter aby kontynuować...")


def future_simple_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Future Simple")
    print("2. Użycie Future Simple")
    print("3. Czasowniki modalne (will/won't)")
    print("0. Powrót do głównego menu")


def future_simple():
    clear_console()
    print("Future Simple opisuje czynności, które będą miały miejsce w przyszłości.")
    print("Czas Future Simple składa się z następujących elementów:")
    print("podmiot + will + czasownik w formie podstawowej")
    print("Oto przykład:")
    print("I will call you tomorrow. - Zadzwonię do Ciebie jutro.")
    input("Wciśnij Enter aby kontynuować...")


def future_simple_usage():
    clear_console()
    print("Użycie Future Simple:")
    print("Czas Future Simple stosujemy, aby wyrazić decyzję podjętą w chwili mówienia lub przewidywanie czegoś w przyszłości.")
    print("Oto przykłady:")
    print("I think it will rain tomorrow. - Myślę, że jutro będzie padać.")
    print("She will probably arrive late. - Prawdopodobnie ona spóźni się.")
    input("Wciśnij Enter aby kontynuować...")


def future_simple_modal_verbs():
    clear_console()
    print("Czasowniki modalne (will/won't):")
    print("W czasie Future Simple używamy will w zdaniach twierdzących oraz won't (will not) w zdaniach przeczących.")
    print("Oto przykłady:")
    print("They will come to the party. - Oni przyjdą na imprezę.")
    print("She won't go to the concert. - Ona nie pójdzie na koncert.")
    input("Wciśnij Enter aby kontynuować...")


def future_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Future Continuous")
    print("2. Użycie Future Continuous")
    print("3. Czasowniki modalne (will be)")
    print("0. Powrót do głównego menu")


def future_continuous():
    clear_console()
    print("Future Continuous opisuje czynności, które będą trwały w określonym momencie w przyszłości.")
    print("Czas Future Continuous składa się z następujących elementów:")
    print("podmiot + will be + czasownik zakończony na -ing")
    print("Oto przykład:")
    print("I will be studying at this time tomorrow. - Jutro o tej porze będę się uczył.")
    input("Wciśnij Enter aby kontynuować...")


def future_continuous_usage():
    clear_console()
    print("Future Continuous Użycie:")
    print("Czasu Future Continuous używamy do opisania czynności, które będą trwały w określonym momencie w przyszłości.")
    print("Oto przykład:")
    print("I will be studying when you arrive. - Będę się uczył, gdy przyjdziesz.")
    input("Wciśnij Enter aby kontynuować...")


def future_continuous_modal_verbs():
    clear_console()
    print("Czasowniki modalne (will be):")
    print("W czasie Future Continuous używamy will be.")
    print("Oto przykłady:")
    print("I will be studying at this time tomorrow. - Jutro o tej porze będę się uczył.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Future Perfect")
    print("2. Użycie Future Perfect")
    print("3. Czasowniki modalne (will have)")
    print("0. Powrót do głównego menu")


def future_perfect():
    clear_console()
    print("Future Perfect opisuje czynności, które zostaną zakończone przed określonym punktem w przyszłości.")
    print("Czas Future Perfect składa się z następujących elementów:")
    print("podmiot + will have + czasownik w trzeciej formie (czasownik regularny: -ed, czasownik nieregularny: 3. forma)")
    print("Oto przykład:")
    print("I will have finished my work by the time you arrive. - Skończę swoją pracę do czasu, gdy przyjedziesz.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_usage():
    clear_console()
    print("Future Perfect Użycie:")
    print("Czasu Future Perfect używamy do opisania czynności, które zostaną zakończone w określonym momencie w przyszłości.")
    print("Oto przykład:")
    print("By the time you get home, I will have finished cooking dinner. - Do czasu, gdy wrócisz do domu, skończę gotować obiad.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_modal_verbs():
    clear_console()
    print("Czasowniki modalne (will have):")
    print("W czasie Future Perfect używamy will have.")
    print("Oto przykłady:")
    print("I will have finished my work by the time you arrive. - Skończę swoją pracę do czasu, gdy przyjedziesz.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_continuous_menu():
    clear_console()
    print("Wybierz jedną z opcji:")
    print("1. Budowa zdania w czasie Future Perfect Continuous")
    print("2. Użycie Future Perfect Continuous")
    print("3. Czasowniki modalne (will have been)")
    print("0. Powrót do głównego menu")


def future_perfect_continuous():
    clear_console()
    print("Future Perfect Continuous opisuje czynności, które będą trwały do pewnego momentu w przyszłości przed inną czynnością.")
    print("Czas Future Perfect Continuous składa się z następujących elementów:")
    print("podmiot + will have been + czasownik zakończony na -ing")
    print("Oto przykład:")
    print("By next year, I will have been studying English for five years. - Do przyszłego roku będę uczył się angielskiego przez pięć lat.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_continuous_usage():
    clear_console()
    print("Future Perfect Continuous Użycie:")
    print("Czasu Future Perfect Continuous używamy do opisania czynności, które będą trwały i miały miejsce przez pewien okres czasu przed określonym momentem w przyszłości.")
    print("Oto przykład:")
    print("By next year, I will have been living in this city for ten years. - Do przyszłego roku będę mieszkał w tym mieście od dziesięciu lat.")
    input("Wciśnij Enter aby kontynuować...")


def future_perfect_continuous_modal_verbs():
    clear_console()
    print("Czasowniki modalne (will have been):")
    print("W czasie Future Perfect Continuous używamy will have been.")
    print("Oto przykłady:")
    print("By next year, I will have been studying English for five years. - Do przyszłego roku będę uczył się angielskiego przez pięć lat.")
    input("Wciśnij Enter aby kontynuować...")



def set_window_position(x, y, width, height, hwnd):
    win32gui.MoveWindow(hwnd, x, y, width, height, True)


def main():
    while True:
        print("Witaj w programie nauki gramatyki!")
        print("\nWybierz czas gramatyczny:")
        print("1 - Czas teraźniejszy (Present Simple)")
        print("2 - Czas teraźniejszy ciągły (Present Continuous)")
        print("3 - Czas teraźniejszy doskonały (Present Perfect)")
        print("4 - Czas przeszły prosty (Past Simple)")
        print("5 - Czas przeszły ciągły (Past Continuous)")
        print("6 - Czas przeszły doskonały (Past Perfect)")
        print("7 - Czas przeszły doskonały ciągły (Past Perfect Continuous)")
        print("8 - Czas przyszły prosty (Future Simple)")
        print("9 - Czas przyszły ciągły (Future Continuous)")
        print("10 - Czas przyszły doskonały (Future Perfect)")
        print("11 - Czas przyszły doskonały ciągły (Future Perfect Continuous)")
        print("12 - Czas teraźniejszy doskonały ciągły (Present_Perfect_Continuous)")
        choice = input("Wybierz czas gramatyczny (1-12) lub 0 aby wyjść: ")
        if choice == '0':
            print("Dziękujemy za skorzystanie z programu. Do widzenia!")
            break
        elif choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= 12:
                if choice == 1:
                    present_simple_menu()
                    sub_choice = input("Wybierz opcję (1-4) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 4:
                            if sub_choice == 1:
                                present_simple()
                            elif sub_choice == 2:
                                present_simple_usage_s()
                            elif sub_choice == 3:
                                present_simple_frequency()
                            elif sub_choice == 4:
                                present_simple_to_be()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 2:
                    present_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                present_continuous()
                            elif sub_choice == 2:
                                present_continuous_usage()
                            elif sub_choice == 3:
                                present_continuous_verb_ing()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 3:
                    present_perfect_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                present_perfect()
                            elif sub_choice == 2:
                                present_perfect_usage()
                            elif sub_choice == 3:
                                present_perfect_differences()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 4:
                    past_simple_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                past_simple()
                            elif sub_choice == 2:
                                past_simple_usage()
                            elif sub_choice == 3:
                                past_simple_regular_irregular()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 5:
                    past_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                past_continuous()
                            elif sub_choice == 2:
                                past_continuous_usage()
                            elif sub_choice == 3:
                                past_continuous_verb_ing()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 6:
                    past_perfect_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                past_perfect()
                            elif sub_choice == 2:
                                past_perfect_usage()
                            elif sub_choice == 3:
                                past_perfect_differences()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 7:
                    past_perfect_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                past_perfect_continuous()
                            elif sub_choice == 2:
                                past_perfect_continuous_usage()
                            elif sub_choice == 3:
                                past_perfect_continuous_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 8:
                    future_simple_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                future_simple()
                            elif sub_choice == 2:
                                future_simple_usage()
                            elif sub_choice == 3:
                                future_simple_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 9:
                    future_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                future_continuous()
                            elif sub_choice == 2:
                                future_continuous_usage()
                            elif sub_choice == 3:
                                future_continuous_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 10:
                    future_perfect_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                future_perfect()
                            elif sub_choice == 2:
                                future_perfect_usage()
                            elif sub_choice == 3:
                                future_perfect_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 11:
                    future_perfect_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                future_perfect_continuous()
                            elif sub_choice == 2:
                                future_perfect_continuous_usage()
                            elif sub_choice == 3:
                                future_perfect_continuous_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                elif choice == 12:
                    present_perfect_continuous_menu()
                    sub_choice = input("Wybierz opcję (1-3) lub 0 aby wrócić: ")
                    if sub_choice == '0':
                        continue
                    elif sub_choice.isdigit():
                        sub_choice = int(sub_choice)
                        if 1 <= sub_choice <= 3:
                            if sub_choice == 1:
                                present_perfect_continuous()
                            elif sub_choice == 2:
                                present_perfect_continuous_usage()
                            elif sub_choice == 3:
                                present_perfect_continuous_modal_verbs()
                        else:
                            print("Niepoprawny wybór")
                    else:
                        print("Niepoprawny wybór")
                else:
                    print("Niepoprawny wybór")
            else:
                print("Niepoprawny wybór")
        else:
            print("Niepoprawny wybór")


main()