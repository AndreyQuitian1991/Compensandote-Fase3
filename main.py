
# UNIVERSITY: Universidad Nacional Abierta y a Distancia (UNAD)
# SCHOOL: Escuela de Ciencias Básicas, Tecnología e Ingeniería
# PROGRAM: Ingeniería de Sistemas
# COURSE: Estructura de Datos
# COURSE CODE: 301305
# PHASE: 3 - Componente práctico - Prácticas simuladas
#
# STUDENT: Anderson Andrey Quitian Pérez
# COLLABORATIVE GROUP: 272
#
# APPLICATION: Compensándote - Affiliate Management System
# APPLICATION MODULE: Caja Compensándote - Control de Afiliados
#
# PROGRAMMING LANGUAGE: Python 3
# GRAPHICAL INTERFACE: Tkinter / ttk
# DATA STRUCTURES: Stack, Queue and List
# STORAGE: Main memory (no database or file storage)
#
# PURPOSE:
# Manage the registration and control of affiliates of the
# Compensándote Family Compensation Fund, calculate affiliation
# fees, organize records using linear data structures, generate
# reports and manage affiliate records through a graphical UI.
#
# FILE: main.py
# PROJECT: Fase3AndreyQuitian



"""Compensandote - Affiliate Management System
Data Structures - Phase 3
All application identifiers and code comments are written in English.
"""

import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datetime import datetime
from collections import deque

# Application colors
BACKGROUND = "#FFEB80"
OLIVE = "#777E17"
BROWN = "#6E5F1E"
GREEN = "#177E53"
DARK_GREEN = "#126642"
TEXT_COLOR = "#444444"
WHITE = "#FFFFFF"

PASSWORD = "Caja"
MINIMUM_INCOME = 1_000_000

STUDENT_NAME = "Anderson Andrey Quitian Pérez"
APPLICATION_NAME = "Fase3AndreyQuitian"
COURSE_NAME = "Data Structures - 301305"
PHASE_NUMBER = "3"


class Affiliate:
    """Stores the information of one affiliate."""

    def __init__(
        self,
        identification_type,
        identification_number,
        full_name,
        current_income,
        desired_service,
        employment_type,
        affiliation_fee,
        affiliation_date
    ):
        self.identification_type = identification_type
        self.identification_number = identification_number
        self.full_name = full_name
        self.current_income = current_income
        self.desired_service = desired_service
        self.employment_type = employment_type
        self.affiliation_fee = affiliation_fee
        self.affiliation_date = affiliation_date


class AffiliateStructures:
    """Manages affiliates using a stack, a queue and a list in memory."""

    def __init__(self):
        self.affiliate_stack = []
        self.affiliate_queue = deque()
        self.affiliate_list = []

    def add_affiliate(self, structure_name, affiliate):
        if structure_name == "Stack":
            self.affiliate_stack.append(affiliate)
        elif structure_name == "Queue":
            self.affiliate_queue.append(affiliate)
        elif structure_name == "List":
            self.affiliate_list.append(affiliate)

    def get_records(self, structure_name):
        if structure_name == "Stack":
            return list(reversed(self.affiliate_stack))
        if structure_name == "Queue":
            return list(self.affiliate_queue)
        if structure_name == "List":
            return list(self.affiliate_list)
        return []

    def remove_from_stack(self):
        return self.affiliate_stack.pop() if self.affiliate_stack else None

    def remove_from_queue(self):
        return self.affiliate_queue.popleft() if self.affiliate_queue else None

    def remove_from_list(self, identification_number):
        for affiliate in self.affiliate_list:
            if affiliate.identification_number == identification_number:
                self.affiliate_list.remove(affiliate)
                return affiliate
        return None

    def get_stack_fee_total(self):
        return sum(
            item.affiliation_fee for item in self.affiliate_stack
        )

    def get_queue_count(self):
        return len(self.affiliate_queue)

    def get_list_average_income(self):
        if not self.affiliate_list:
            return 0
        return (
            sum(item.current_income for item in self.affiliate_list)
            / len(self.affiliate_list)
        )

    def identification_exists(self, identification_number):
        all_affiliates = (
            self.affiliate_stack
            + list(self.affiliate_queue)
            + self.affiliate_list
        )
        return any(
            item.identification_number == identification_number
            for item in all_affiliates
        )


class CompensandoteApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login - Compensándote")
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        self.structures = AffiliateStructures()
        self.selected_structure = tk.StringVar(value="List")

        self.create_login_window()

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def create_login_window(self):
        self.clear_window()

        self.root.title("Login - Compensándote")
        self.root.geometry("650x650")
        self.root.resizable(False, False)
        self.root.configure(bg=BACKGROUND)

        tk.Label(
            self.root,
            text="COMPENSÁNDOTE",
            font=("Arial", 24, "bold"),
            bg=BACKGROUND,
            fg=OLIVE
        ).pack(pady=(22, 5))

        tk.Label(
            self.root,
            text="AFFILIATE MANAGEMENT SYSTEM",
            font=("Arial", 12, "bold"),
            bg=BROWN,
            fg=WHITE,
            padx=14,
            pady=7
        ).pack(pady=(0, 16))

        tk.Label(
            self.root,
            text="Welcome!",
            font=("Arial", 14, "bold"),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        ).pack(pady=(0, 4))

        tk.Label(
            self.root,
            text="Enter your password to continue",
            font=("Arial", 10),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        ).pack(pady=(0, 10))

        # Academic project information
        info_frame = tk.Frame(
            self.root,
            bg=WHITE,
            highlightbackground=BROWN,
            highlightthickness=1,
            padx=18,
            pady=10
        )
        info_frame.pack(fill="x", padx=55, pady=(0, 16))

        info_rows = [
            ("Application:", APPLICATION_NAME),
            ("Student:", STUDENT_NAME),
            ("Course:", COURSE_NAME),
            ("Phase:", PHASE_NUMBER),
            ("Date:", datetime.now().strftime("%B %d, %Y")),
        ]

        for row_index, (label_text, value_text) in enumerate(info_rows):
            tk.Label(
                info_frame,
                text=label_text,
                font=("Arial", 10, "bold"),
                bg=WHITE,
                fg=TEXT_COLOR,
                anchor="w",
                width=14
            ).grid(
                row=row_index,
                column=0,
                sticky="w",
                padx=(0, 8),
                pady=3
            )

            tk.Label(
                info_frame,
                text=value_text,
                font=("Arial", 10),
                bg=WHITE,
                fg=TEXT_COLOR,
                anchor="w"
            ).grid(
                row=row_index,
                column=1,
                sticky="w",
                pady=3
            )

        tk.Label(
            self.root,
            text="Password",
            font=("Arial", 10),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        ).pack(anchor="w", padx=58)

        self.password_entry = tk.Entry(
            self.root,
            show="*",
            font=("Arial", 12),
            width=32,
            justify="left"
        )
        self.password_entry.pack(pady=(5, 8), ipady=4)
        self.password_entry.focus_set()

        tk.Label(
            self.root,
            text="Password masked (* * *)",
            font=("Arial", 9),
            bg=BACKGROUND,
            fg=TEXT_COLOR
        ).pack(pady=(0, 7))

        button_frame = tk.Frame(self.root, bg=BACKGROUND)
        button_frame.pack(pady=5)

        tk.Button(
            button_frame,
            text="Login  →",
            font=("Arial", 11, "bold"),
            bg=GREEN,
            fg=WHITE,
            activebackground=DARK_GREEN,
            activeforeground=WHITE,
            width=18,
            height=2,
            command=self.login
        ).grid(row=0, column=0, padx=6)

        tk.Button(
            button_frame,
            text="About",
            width=12,
            command=self.show_about
        ).grid(row=0, column=1, padx=6, ipady=8)

        tk.Button(
            button_frame,
            text="Exit",
            width=12,
            command=self.root.destroy
        ).grid(row=0, column=2, padx=6, ipady=8)

        tk.Label(
            self.root,
            text="UNAD - Data Structures 301305",
            font=("Arial", 9),
            bg=BACKGROUND,
            fg=BROWN
        ).pack(side="bottom", pady=12)

        self.password_entry.bind(
            "<Return>",
            lambda event: self.login()
        )

    def login(self):
        if self.password_entry.get() == PASSWORD:
            self.create_affiliate_form()
        else:
            messagebox.showerror(
                "Login error",
                "Incorrect password. Please try again."
            )
            self.password_entry.delete(0, tk.END)
            self.password_entry.focus_set()

    def show_about(self):
        messagebox.showinfo(
            "About - Compensándote",
            f"Application: {APPLICATION_NAME}\n"
            f"Student: {STUDENT_NAME}\n"
            f"Course: {COURSE_NAME}\n"
            f"Phase: {PHASE_NUMBER}\n"
            f"Date: {datetime.now().strftime('%B %d, %Y')}\n"
            "Collaborative group: To be confirmed"
        )

    def create_affiliate_form(self):
        self.clear_window()

        self.root.title("Compensándote - Affiliate Registration")
        self.root.geometry("1050x790")
        self.root.minsize(900, 700)
        self.root.configure(bg=BACKGROUND)

        main_frame = tk.Frame(
            self.root,
            bg=BACKGROUND,
            padx=12,
            pady=12
        )
        main_frame.pack(fill="both", expand=True)

        tk.Label(
            main_frame,
            text="COMPENSÁNDOTE",
            font=("Arial", 20, "bold"),
            bg=BACKGROUND,
            fg=OLIVE
        ).pack(pady=(0, 3))

        tk.Label(
            main_frame,
            text="AFFILIATE REGISTRATION",
            font=("Arial", 12, "bold"),
            bg=BROWN,
            fg=WHITE,
            padx=10,
            pady=5
        ).pack(pady=(0, 12))

        form = tk.Frame(main_frame, bg=BACKGROUND)
        form.pack(fill="x", anchor="w")

        labels = [
            "Identification type:",
            "Identification number:",
            "Full name:",
            "Current income (COP):",
            "Desired service:",
            "Employment type:",
            "Affiliation date (dd/mm/yyyy):",
            "Affiliation fee (COP):"
        ]

        for row, label_text in enumerate(labels):
            tk.Label(
                form,
                text=label_text,
                bg=BACKGROUND,
                fg=TEXT_COLOR
            ).grid(
                row=row,
                column=0,
                sticky="w",
                padx=8,
                pady=5
            )

        self.id_type = ttk.Combobox(
            form,
            values=["CC", "CE", "NUIP", "PAS"],
            state="readonly",
            width=28
        )
        self.id_type.grid(
            row=0, column=1, sticky="w", padx=8, pady=5
        )
        self.id_type.set("CC")

        self.id_number = tk.Entry(form, width=31)
        self.id_number.grid(
            row=1, column=1, sticky="w", padx=8, pady=5
        )

        self.full_name = tk.Entry(form, width=31)
        self.full_name.grid(
            row=2, column=1, sticky="w", padx=8, pady=5
        )

        self.income = tk.Entry(form, width=31)
        self.income.grid(
            row=3, column=1, sticky="w", padx=8, pady=5
        )

        self.service = ttk.Combobox(
            form,
            values=[
                "Unemployment subsidy",
                "Park admission",
                "Training course",
                "Travel package",
                "Preventive medicine"
            ],
            state="readonly",
            width=28
        )
        self.service.grid(
            row=4, column=1, sticky="w", padx=8, pady=5
        )
        self.service.current(0)

        self.employment_type = tk.StringVar(value="Employee")

        employment_frame = tk.Frame(form, bg=BACKGROUND)
        employment_frame.grid(
            row=5, column=1, sticky="w", padx=8, pady=5
        )

        tk.Radiobutton(
            employment_frame,
            text="Employee",
            variable=self.employment_type,
            value="Employee",
            bg=BACKGROUND,
            activebackground=BACKGROUND
        ).pack(side="left")

        tk.Radiobutton(
            employment_frame,
            text="Independent",
            variable=self.employment_type,
            value="Independent",
            bg=BACKGROUND,
            activebackground=BACKGROUND
        ).pack(side="left", padx=10)

        self.affiliation_date = tk.Entry(form, width=31)
        self.affiliation_date.grid(
            row=6, column=1, sticky="w", padx=8, pady=5
        )
        self.affiliation_date.insert(
            0, datetime.now().strftime("%d/%m/%Y")
        )

        self.fee_label = tk.Label(
            form,
            text="$0",
            font=("Arial", 11, "bold"),
            bg=BACKGROUND,
            fg=OLIVE
        )
        self.fee_label.grid(
            row=7, column=1, sticky="w", padx=8, pady=5
        )

        tk.Button(
            form,
            text="Calculate fee",
            bg=GREEN,
            fg=WHITE,
            activebackground=DARK_GREEN,
            command=self.calculate_fee
        ).grid(
            row=8, column=1, sticky="w", padx=8, pady=8
        )

        tk.Label(
            form,
            text="Data structure:",
            bg=BACKGROUND,
            fg=TEXT_COLOR
        ).grid(
            row=9, column=0, sticky="w", padx=8, pady=5
        )

        self.structure_combo = ttk.Combobox(
            form,
            textvariable=self.selected_structure,
            values=["Stack", "Queue", "List"],
            state="readonly",
            width=28
        )
        self.structure_combo.grid(
            row=9, column=1, sticky="w", padx=8, pady=5
        )
        self.structure_combo.bind(
            "<<ComboboxSelected>>",
            lambda event: self.refresh_table()
        )

        button_frame = tk.Frame(main_frame, bg=BACKGROUND)
        button_frame.pack(pady=8)

        tk.Button(
            button_frame,
            text="Register affiliate",
            bg=GREEN,
            fg=WHITE,
            activebackground=DARK_GREEN,
            command=self.register_affiliate,
            width=18
        ).grid(row=0, column=0, padx=5)

        tk.Button(
            button_frame,
            text="Clear fields",
            command=self.clear_fields,
            width=14
        ).grid(row=0, column=1, padx=5)

        tk.Button(
            button_frame,
            text="Remove affiliate",
            command=self.remove_affiliate,
            width=15
        ).grid(row=0, column=2, padx=5)

        tk.Button(
            button_frame,
            text="Reports",
            command=self.show_reports,
            width=12
        ).grid(row=0, column=3, padx=5)

        tk.Button(
            button_frame,
            text="Back to login",
            command=self.create_login_window,
            width=14
        ).grid(row=0, column=4, padx=5)

        tk.Label(
            main_frame,
            text="Registered affiliates",
            font=("Arial", 11, "bold"),
            bg=BACKGROUND,
            fg=BROWN
        ).pack(pady=(8, 4))

        columns = (
            "id", "name", "income", "employment",
            "fee", "service", "date"
        )

        self.affiliate_table = ttk.Treeview(
            main_frame,
            columns=columns,
            show="headings",
            height=8
        )

        headings = {
            "id": "Identification",
            "name": "Full name",
            "income": "Income",
            "employment": "Employment",
            "fee": "Fee",
            "service": "Service",
            "date": "Affiliation date"
        }

        widths = {
            "id": 135,
            "name": 150,
            "income": 115,
            "employment": 105,
            "fee": 100,
            "service": 190,
            "date": 110
        }

        for column in columns:
            self.affiliate_table.heading(
                column, text=headings[column]
            )
            self.affiliate_table.column(
                column,
                width=widths[column],
                anchor="w"
            )

        self.affiliate_table.pack(
            fill="both",
            expand=True,
            pady=5
        )

        self.refresh_table()

    def parse_income(self, show_message=True):
        income_text = (
            self.income.get()
            .strip()
            .replace(",", "")
            .replace("$", "")
        )

        try:
            income = float(income_text)

            if income < MINIMUM_INCOME:
                raise ValueError

            return income

        except ValueError:
            if show_message:
                messagebox.showerror(
                    "Invalid income",
                    "Enter a numeric income of at least $1,000,000 COP."
                )
            return None

    def calculate_fee(self, show_message=True):
        income = self.parse_income(show_message)

        if income is None:
            return None

        if self.employment_type.get() == "Employee":
            if income <= 2_000_000:
                base_fee = 45_000
            elif income <= 3_000_000:
                base_fee = 60_000
            elif income <= 4_000_000:
                base_fee = 75_000
            elif income <= 5_000_000:
                base_fee = 90_000
            else:
                base_fee = 150_000
        else:
            if income <= 2_000_000:
                base_fee = 10_000
            elif income <= 3_000_000:
                base_fee = 20_000
            elif income <= 4_000_000:
                base_fee = 30_000
            elif income <= 5_000_000:
                base_fee = 40_000
            else:
                base_fee = 80_000

        service = self.service.get()

        surcharges = {
            "Unemployment subsidy": 0,
            "Park admission": 2_500,
            "Training course": 7_500,
            "Travel package": 10_000
        }

        if service == "Preventive medicine":
            total_fee = base_fee + income * 0.10
        else:
            total_fee = base_fee + surcharges.get(service, 0)

        self.fee_label.config(text=f"${total_fee:,.0f}")
        return total_fee

    def register_affiliate(self):
        id_type = self.id_type.get().strip()
        id_number = self.id_number.get().strip()
        name = self.full_name.get().strip()
        service = self.service.get().strip()
        employment = self.employment_type.get()
        date_text = self.affiliation_date.get().strip()

        if not all([
            id_type,
            id_number,
            name,
            self.income.get().strip(),
            service,
            date_text
        ]):
            messagebox.showerror(
                "Missing information",
                "Please complete all required fields."
            )
            return

        if not id_number.isdigit():
            messagebox.showerror(
                "Invalid identification",
                "Identification number must contain digits only."
            )
            return

        if not any(character.isalpha() for character in name) or not all(
            character.isalpha() or character.isspace()
            for character in name
        ):
            messagebox.showerror(
                "Invalid name",
                "Full name must contain letters and spaces only."
            )
            return

        income = self.parse_income()
        if income is None:
            return

        try:
            parsed_date = datetime.strptime(
                date_text, "%d/%m/%Y"
            )
            if parsed_date.strftime("%d/%m/%Y") != date_text:
                raise ValueError
        except ValueError:
            messagebox.showerror(
                "Invalid date",
                "Enter a valid date in dd/mm/yyyy format."
            )
            return

        if self.structures.identification_exists(id_number):
            messagebox.showerror(
                "Duplicate identification",
                "An affiliate with this identification is already registered."
            )
            return

        fee = self.calculate_fee(show_message=False)
        if fee is None:
            return

        affiliate = Affiliate(
            id_type,
            id_number,
            name,
            income,
            service,
            employment,
            fee,
            date_text
        )

        structure_name = self.selected_structure.get()
        self.structures.add_affiliate(
            structure_name, affiliate
        )

        self.refresh_table()

        messagebox.showinfo(
            "Registration successful",
            f"Affiliate {name} registered in {structure_name}."
        )

        self.clear_fields()

    def refresh_table(self):
        if not hasattr(self, "affiliate_table"):
            return

        for item in self.affiliate_table.get_children():
            self.affiliate_table.delete(item)

        for affiliate in self.structures.get_records(
            self.selected_structure.get()
        ):
            self.affiliate_table.insert(
                "",
                "end",
                values=(
                    f"{affiliate.identification_type} "
                    f"{affiliate.identification_number}",
                    affiliate.full_name,
                    f"${affiliate.current_income:,.0f}",
                    affiliate.employment_type,
                    f"${affiliate.affiliation_fee:,.0f}",
                    affiliate.desired_service,
                    affiliate.affiliation_date
                )
            )

    def remove_affiliate(self):
        structure_name = self.selected_structure.get()
        records = self.structures.get_records(structure_name)

        if not records:
            messagebox.showwarning(
                "No affiliates",
                f"There are no affiliates in {structure_name}."
            )
            return

        if structure_name == "Stack":
            candidate = self.structures.affiliate_stack[-1]
            prompt = (
                "Remove the last registered affiliate: "
                f"{candidate.full_name}?"
            )

            if not messagebox.askyesno(
                "Confirm removal", prompt
            ):
                return

            removed = self.structures.remove_from_stack()

        elif structure_name == "Queue":
            candidate = self.structures.affiliate_queue[0]
            prompt = (
                "Remove the first affiliate in the queue: "
                f"{candidate.full_name}?"
            )

            if not messagebox.askyesno(
                "Confirm removal", prompt
            ):
                return

            removed = self.structures.remove_from_queue()

        else:
            identification_number = simpledialog.askstring(
                "Remove affiliate",
                "Enter the identification number to remove:",
                parent=self.root
            )

            if identification_number is None:
                return

            identification_number = identification_number.strip()

            candidate = next(
                (
                    item
                    for item in self.structures.affiliate_list
                    if item.identification_number == identification_number
                ),
                None
            )

            if candidate is None:
                messagebox.showwarning(
                    "Not found",
                    "No affiliate with that identification was found in List."
                )
                return

            if not messagebox.askyesno(
                "Confirm removal",
                f"Remove affiliate {candidate.full_name}?"
            ):
                return

            removed = self.structures.remove_from_list(
                identification_number
            )

        if removed is not None:
            self.refresh_table()
            messagebox.showinfo(
                "Removal successful",
                f"Affiliate {removed.full_name} was removed "
                f"from {structure_name}."
            )

    def show_reports(self):
        report_text = (
            "COMPENSÁNDOTE - REPORTS\n\n"
            "STACK REPORT\n"
            f"Total affiliation fees: "
            f"${self.structures.get_stack_fee_total():,.0f}\n"
            f"Number of affiliates: "
            f"{len(self.structures.affiliate_stack)}\n\n"
            "QUEUE REPORT\n"
            f"Number of affiliates: "
            f"{self.structures.get_queue_count()}\n\n"
            "LIST REPORT\n"
            f"Number of affiliates: "
            f"{len(self.structures.affiliate_list)}\n"
            f"Average current income: "
            f"${self.structures.get_list_average_income():,.0f}"
        )

        messagebox.showinfo(
            "Affiliate reports",
            report_text 
        )

    def clear_fields(self):
        self.id_type.set("CC")
        self.id_number.delete(0, tk.END)
        self.full_name.delete(0, tk.END)
        self.income.delete(0, tk.END)
        self.service.current(0)
        self.employment_type.set("Employee")
        self.affiliation_date.delete(0, tk.END)
        self.affiliation_date.insert(
            0, datetime.now().strftime("%d/%m/%Y")
        )
        self.fee_label.config(text="$0")


def main():
    root = tk.Tk()
    CompensandoteApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
