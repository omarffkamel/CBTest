import streamlit as st

# Define the tasks
tasks = [
    {
        'rule': 'If a card has a vowel on one side, then it has an even number on the other side.',
        'cards': ['A', 'K', '4', '7'],
        'cards_that_confirm': ['A', '4'],
        'cards_that_falsify': ['7'],
    },
    {
        'rule': 'If a person is drinking alcohol, then they must be over 21 years old.',
        'cards': ['Drinking alcohol', 'Drinking soda', '22 years old', '17 years old'],
        'cards_that_confirm': ['Drinking alcohol', '22 years old'],
        'cards_that_falsify': ['17 years old'],
    },
    {
        'rule': 'If a car has a D sticker, then it is from Germany.',
        'cards': ['D sticker', 'F sticker', 'German car', 'French car'],
        'cards_that_confirm': ['D sticker', 'German car'],
        'cards_that_falsify': ['French car'],
    },
    {
        'rule': 'If an animal is a bird, then it can fly.',
        'cards': ['Bird', 'Bat', 'Can fly', 'Cannot fly'],
        'cards_that_confirm': ['Bird', 'Can fly'],
        'cards_that_falsify': ['Cannot fly'],
    },
    {
        'rule': 'If a shape is a square, then it has four sides.',
        'cards': ['Square', 'Triangle', 'Four sides', 'Three sides'],
        'cards_that_confirm': ['Square', 'Four sides'],
        'cards_that_falsify': ['Three sides'],
    },
    {
        'rule': 'If a person studies hard, then they will pass the exam.',
        'cards': ['Studies hard', 'Does not study', 'Passes exam', 'Fails exam'],
        'cards_that_confirm': ['Studies hard', 'Passes exam'],
        'cards_that_falsify': ['Fails exam'],
    },
    {
        'rule': 'If a container is sealed, then it is airtight.',
        'cards': ['Sealed', 'Unsealed', 'Airtight', 'Not airtight'],
        'cards_that_confirm': ['Sealed', 'Airtight'],
        'cards_that_falsify': ['Not airtight'],
    },
    {
        'rule': 'If a person is a teacher, then they work at a school.',
        'cards': ['Teacher', 'Engineer', 'Works at school', 'Works at office'],
        'cards_that_confirm': ['Teacher', 'Works at school'],
        'cards_that_falsify': ['Works at office'],
    },
    {
        'rule': 'If a fruit is an apple, then it is red.',
        'cards': ['Apple', 'Banana', 'Red', 'Yellow'],
        'cards_that_confirm': ['Apple', 'Red'],
        'cards_that_falsify': ['Yellow'],
    },
    {
        'rule': 'If a vehicle is a motorcycle, then it has two wheels.',
        'cards': ['Motorcycle', 'Car', 'Two wheels', 'Four wheels'],
        'cards_that_confirm': ['Motorcycle', 'Two wheels'],
        'cards_that_falsify': ['Four wheels'],
    },
    {
        'rule': 'If a person is married, then they wear a ring.',
        'cards': ['Married', 'Single', 'Wears ring', 'Does not wear ring'],
        'cards_that_confirm': ['Married', 'Wears ring'],
        'cards_that_falsify': ['Does not wear ring'],
    },
]

def main():
    st.title("The Wason Selection Task")

    st.write("""

    You will be presented with 10 tasks. For each task, you will see a rule and four cards.

    Select the cards you think need to be turned over to test whether the rule is true or false.

    At the end, you will receive a metric of your confirmation bias.
    """)

    user_selections = []

    for idx, task in enumerate(tasks):
        st.header(f"Task {idx + 1}")
        st.write(f"**Rule:** {task['rule']}")
        st.write("**Cards:**")

        # Create checkboxes for each card
        selections = {}
        for card in task['cards']:
            selections[card] = st.checkbox(card, key=f"{idx}_{card}")

        # Store the selections
        selected_cards = [card for card, selected in selections.items() if selected]
        user_selections.append({
            'task_index': idx,
            'selected_cards': selected_cards
        })

    if st.button("Submit"):
        # Process the selections and compute confirmation bias score
        total_tasks = len(tasks)
        confirmation_bias_count = 0

        for idx, selection in enumerate(user_selections):
            task = tasks[idx]
            selected_cards = selection['selected_cards']

            # Check if the user selected any falsifying cards
            falsifying_cards_selected = [card for card in selected_cards if card in task['cards_that_falsify']]

            if not falsifying_cards_selected:
                # User did not select falsifying cards
                confirmation_bias_count += 1

        # Compute confirmation bias score
        confirmation_bias_score = (confirmation_bias_count / total_tasks) * 100

        st.header("Results")
        st.write(f" Confirmation Bias Score : **{confirmation_bias_score:.2f}%**")
    

       
if __name__ == "__main__":
    main()