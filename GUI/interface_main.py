from tkinter import Tk, LabelFrame, Label, StringVar, Entry, Button, ttk

import engine.tokenization
import engine.semantic_analyze
import engine.distance


class InterfaceMain:
    def __init__(self, model):
        self._model = model
        self.RESULTS_NUMBER = 16
        self.root = Tk()
        self.input_field = None
        self.semantic_choice_field = None
        self.tokenization_choice_field = None
        self.distance_choice_field = None
        self.results = []

    def draw(self):
        self._init_root()
        self._draw_user_input()
        self._draw_options()
        self._draw_response()
        self.root.mainloop()

    def _init_root(self):
        self.root.geometry("600x500")
        self.root.title("Semantic analyse")

    def _draw_user_input(self):
        function_frame = LabelFrame(self.root, text="Input", width=260, height=130)
        function_frame.place(x=20, y=20)

        self._draw_label(text='Type phrase to search', label_x=40, label_y=40)

        self.input_field = Entry(self.root, width=20, textvariable=StringVar())
        self.input_field.place(x=40, y=60)

        search_button = Button(self.root, text='Search', width=8, height=1, command=self._generate_semantic_results)
        search_button.place(x=40, y=100)

    def _draw_label(self, text, label_x, label_y, font_size=10, text_variable=None):
        question_label = Label(self.root, text=text, textvariable=text_variable)
        question_label.config(font=("Arial", font_size))
        question_label.place(x=label_x, y=label_y)

    def _generate_semantic_results(self):
        # pass this values to semantic search algorithm
        text = self.input_field.get()
        self._model.create_model(self.tokenization_choice_field.current(), self.semantic_choice_field.current())
        results = self._model.search(text, self.distance_choice_field.current())
        for index, result in enumerate(results):
            self.results[index].set(f"{index + 1}. {result}")

    def _draw_options(self):
        function_frame = LabelFrame(self.root, text="Options", width=260, height=250)
        function_frame.place(x=20, y=200)

        self.semantic_choice_field = self._generate_combobox(label_text="Choose tokenization type",
                                                             label_y=220,
                                                             values=engine.tokenization.TokenizationTypes.get_names())

        self.tokenization_choice_field = self._generate_combobox(label_text="Choose semantic analyze type",
                                                                 label_y=300,
                                                                 values=engine.semantic_analyze.SemanticTypes.get_names())

        self.distance_choice_field = self._generate_combobox(label_text="Choose distance type",
                                                             label_y=380,
                                                             values=engine.distance.DistanceMetric.get_names())

    def _generate_combobox(self, label_text, label_y, values):
        self._draw_label(text=label_text, label_x=40, label_y=label_y)
        combobox_field = ttk.Combobox(self.root, values=values, state="readonly")
        combobox_field.current(0)
        combobox_field.place(x=40, y=label_y + 20)
        return combobox_field

    def _draw_response(self):
        function_frame = LabelFrame(self.root, text="Results", width=260, height=430)
        function_frame.place(x=310, y=20)

        for i in range(self.RESULTS_NUMBER):
            text_variable = StringVar()
            text_variable.set(f"{i + 1}.")
            self._draw_label(text=f"", label_x=330, label_y=25 * (i + 1) + 20, font_size=12,
                             text_variable=text_variable)
            self.results.append(text_variable)
