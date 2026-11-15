import tkinter as tk
from tkinter import ttk, messagebox

# Sports Event Management System
# A Tkinter frontend with in-memory participant records.

BG = "#F3F6FB"
CARD = "#FFFFFF"
PRIMARY = "#2457A7"
PRIMARY_DARK = "#183F7A"
TEXT = "#1E293B"
MUTED = "#64748B"
BORDER = "#DCE4EF"

SPORTS = [
    "Select a sport",
    "Cricket",
    "Football",
    "Basketball",
    "Badminton",
    "Volleyball",
    "Athletics",
    "Chess",
    "Tennis",
]


class SportsEventApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sports Event Management System")
        self.root.geometry("1050x690")
        self.root.minsize(900, 620)
        self.root.configure(bg=BG)

        self.participants = {}  # participant_id -> participant details
        self.selected_id = None

        self._setup_styles()
        self._build_ui()

    def _setup_styles(self):
        style = ttk.Style()
        style.theme_use("clam")
        style.configure(
            "TEntry",
            padding=9,
            fieldbackground="#FFFFFF",
            foreground=TEXT,
            bordercolor=BORDER,
            lightcolor=BORDER,
            darkcolor=BORDER,
        )
        style.configure(
            "TCombobox",
            padding=8,
            fieldbackground="#FFFFFF",
            background="#FFFFFF",
            foreground=TEXT,
            arrowcolor=PRIMARY,
        )
        style.map(
            "TCombobox",
            fieldbackground=[("readonly", "#FFFFFF")],
            selectbackground=[("readonly", "#FFFFFF")],
            selectforeground=[("readonly", TEXT)],
        )
        style.configure(
            "Primary.TButton",
            background=PRIMARY,
            foreground="#FFFFFF",
            padding=(15, 10),
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map("Primary.TButton", background=[("active", PRIMARY_DARK)])
        style.configure(
            "Secondary.TButton",
            background="#E8EEF8",
            foreground=PRIMARY_DARK,
            padding=(15, 10),
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map("Secondary.TButton", background=[("active", "#D8E3F3")])
        style.configure(
            "Danger.TButton",
            background="#FCE8E8",
            foreground="#B42318",
            padding=(15, 10),
            font=("Segoe UI", 10, "bold"),
            borderwidth=0,
        )
        style.map("Danger.TButton", background=[("active", "#F8D4D4")])

    def _build_ui(self):
        # Header
        header = tk.Frame(self.root, bg=PRIMARY, height=112)
        header.pack(fill="x")
        header.pack_propagate(False)

        tk.Label(
            header,
            text="SPORTS EVENT MANAGEMENT",
            bg=PRIMARY,
            fg="white",
            font=("Segoe UI", 21, "bold"),
        ).pack(anchor="w", padx=30, pady=(22, 2))

        tk.Label(
            header,
            text="Register and manage student participation in sports events",
            bg=PRIMARY,
            fg="#DCE9FF",
            font=("Segoe UI", 10),
        ).pack(anchor="w", padx=31)

        # Main content
        body = tk.Frame(self.root, bg=BG)
        body.pack(fill="both", expand=True, padx=24, pady=20)

        left = tk.Frame(body, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        left.pack(side="left", fill="y", padx=(0, 16))
        left.configure(width=365)
        left.pack_propagate(False)

        right = tk.Frame(body, bg=CARD, highlightbackground=BORDER, highlightthickness=1)
        right.pack(side="left", fill="both", expand=True)

        self._build_form(left)
        self._build_records(right)

        # Footer
        footer = tk.Frame(self.root, bg=BG)
        footer.pack(fill="x", padx=26, pady=(0, 12))
        self.status_var = tk.StringVar(value="Ready — add a participant to get started.")
        tk.Label(
            footer,
            textvariable=self.status_var,
            bg=BG,
            fg=MUTED,
            font=("Segoe UI", 9),
        ).pack(side="left")
        self.count_var = tk.StringVar(value="Participants: 0")
        tk.Label(
            footer,
            textvariable=self.count_var,
            bg=BG,
            fg=PRIMARY_DARK,
            font=("Segoe UI", 9, "bold"),
        ).pack(side="right")

    def _section_title(self, parent, title, subtitle=None):
        tk.Label(
            parent,
            text=title,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 14, "bold"),
        ).pack(anchor="w", padx=22, pady=(20, 2))
        if subtitle:
            tk.Label(
                parent,
                text=subtitle,
                bg=CARD,
                fg=MUTED,
                font=("Segoe UI", 9),
            ).pack(anchor="w", padx=22, pady=(0, 14))

    def _field_label(self, parent, text):
        tk.Label(
            parent,
            text=text,
            bg=CARD,
            fg=TEXT,
            font=("Segoe UI", 9, "bold"),
        ).pack(anchor="w", padx=22, pady=(9, 5))

    def _build_form(self, parent):
        self._section_title(
            parent,
            "Participant Details",
            "Enter the student's information below.",
        )

        self._field_label(parent, "Participant ID *")
        self.id_entry = ttk.Entry(parent)
        self.id_entry.pack(fill="x", padx=22)

        self._field_label(parent, "Student Name *")
        self.name_entry = ttk.Entry(parent)
        self.name_entry.pack(fill="x", padx=22)

        self._field_label(parent, "Sport Name")
        self.sport_var = tk.StringVar(value=SPORTS[0])
        self.sport_menu = ttk.Combobox(
            parent,
            textvariable=self.sport_var,
            values=SPORTS,
            state="readonly",
        )
        self.sport_menu.pack(fill="x", padx=22)

        self._field_label(parent, "Age *")
        self.age_entry = ttk.Entry(parent)
        self.age_entry.pack(fill="x", padx=22)

        self._field_label(parent, "Participation Type")
        self.participation_var = tk.StringVar(value="Individual")
        radio_frame = tk.Frame(parent, bg=CARD)
        radio_frame.pack(fill="x", padx=18, pady=(2, 10))
        for value in ("Individual", "Team"):
            tk.Radiobutton(
                radio_frame,
                text=value,
                variable=self.participation_var,
                value=value,
                bg=CARD,
                fg=TEXT,
                activebackground=CARD,
                selectcolor="#E8EEF8",
                font=("Segoe UI", 9),
            ).pack(side="left", padx=5)

        button_frame = tk.Frame(parent, bg=CARD)
        button_frame.pack(fill="x", padx=22, pady=(12, 6))
        ttk.Button(
            button_frame, text="Add Participant", style="Primary.TButton",
            command=self.add_participant
        ).pack(fill="x", pady=4)
        ttk.Button(
            button_frame, text="Update Details", style="Secondary.TButton",
            command=self.update_participant
        ).pack(fill="x", pady=4)
        ttk.Button(
            button_frame, text="Remove Participant", style="Danger.TButton",
            command=self.remove_participant
        ).pack(fill="x", pady=4)
        ttk.Button(
            button_frame, text="Clear Form", style="Secondary.TButton",
            command=self.clear_form
        ).pack(fill="x", pady=4)

        tk.Label(
            parent,
            text="* Required fields",
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 8),
        ).pack(anchor="w", padx=22, pady=(8, 16))

    def _build_records(self, parent):
        self._section_title(
            parent,
            "Registered Participants",
            "Search by participant ID or select a record to edit it.",
        )

        search_frame = tk.Frame(parent, bg=CARD)
        search_frame.pack(fill="x", padx=22, pady=(0, 14))

        self.search_entry = ttk.Entry(search_frame)
        self.search_entry.pack(side="left", fill="x", expand=True, ipady=2)
        self.search_entry.insert(0, "Enter Participant ID")
        self.search_entry.bind("<FocusIn>", self._clear_search_placeholder)
        self.search_entry.bind("<Return>", lambda event: self.search_participant())

        ttk.Button(
            search_frame,
            text="Search",
            style="Primary.TButton",
            command=self.search_participant,
        ).pack(side="left", padx=(8, 0))
        ttk.Button(
            search_frame,
            text="Show All",
            style="Secondary.TButton",
            command=self.display_all,
        ).pack(side="left", padx=(8, 0))

        list_frame = tk.Frame(parent, bg=CARD)
        list_frame.pack(fill="both", expand=True, padx=22, pady=(0, 22))

        headings = tk.Frame(list_frame, bg="#EAF0F8")
        headings.pack(fill="x")
        for label, width in [
            ("PARTICIPANT ID", 18),
            ("STUDENT NAME", 22),
            ("SPORT", 15),
            ("AGE", 6),
            ("TYPE", 12),
        ]:
            tk.Label(
                headings,
                text=label,
                width=width,
                anchor="w",
                bg="#EAF0F8",
                fg=PRIMARY_DARK,
                font=("Segoe UI", 8, "bold"),
                padx=7,
                pady=10,
            ).pack(side="left")

        list_container = tk.Frame(list_frame, bg=CARD)
        list_container.pack(fill="both", expand=True)

        self.listbox = tk.Listbox(
            list_container,
            font=("Consolas", 9),
            bg="#FFFFFF",
            fg=TEXT,
            selectbackground="#DCE9FF",
            selectforeground=TEXT,
            activestyle="none",
            relief="flat",
            highlightthickness=1,
            highlightbackground=BORDER,
            height=16,
        )
        scrollbar = ttk.Scrollbar(
            list_container, orient="vertical", command=self.listbox.yview
        )
        self.listbox.configure(yscrollcommand=scrollbar.set)
        self.listbox.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        self.listbox.bind("<<ListboxSelect>>", self.load_selected)

        tk.Label(
            parent,
            text="Tip: Select a participant from the list to load their details into the form.",
            bg=CARD,
            fg=MUTED,
            font=("Segoe UI", 8),
        ).pack(anchor="w", padx=22, pady=(0, 16))

    def _clear_search_placeholder(self, _event):
        if self.search_entry.get() == "Enter Participant ID":
            self.search_entry.delete(0, tk.END)

    def _read_form(self):
        participant_id = self.id_entry.get().strip()
        name = self.name_entry.get().strip()
        sport = self.sport_var.get()
        age_text = self.age_entry.get().strip()
        participation = self.participation_var.get()

        if not participant_id:
            messagebox.showwarning("Validation", "Participant ID is mandatory.")
            self.id_entry.focus_set()
            return None
        if not name:
            messagebox.showwarning("Validation", "Student name is mandatory.")
            self.name_entry.focus_set()
            return None
        if sport == SPORTS[0]:
            messagebox.showwarning("Validation", "Please select a sport.")
            self.sport_menu.focus_set()
            return None
        try:
            age = int(age_text)
            if age <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning(
                "Validation", "Age must be a valid positive integer."
            )
            self.age_entry.focus_set()
            return None

        return {
            "id": participant_id,
            "name": name,
            "sport": sport,
            "age": age,
            "participation": participation,
        }

    def add_participant(self):
        record = self._read_form()
        if record is None:
            return
        if record["id"] in self.participants:
            messagebox.showerror(
                "Duplicate ID", "This Participant ID already exists."
            )
            return

        self.participants[record["id"]] = record
        self.display_all()
        self.clear_form()
        self.status_var.set(f"Participant {record['id']} added successfully.")

    def search_participant(self):
        participant_id = self.search_entry.get().strip()
        if not participant_id or participant_id == "Enter Participant ID":
            messagebox.showinfo("Search", "Enter a Participant ID to search.")
            return

        record = self.participants.get(participant_id)
        if record is None:
            messagebox.showinfo(
                "Not Found", f"No participant found with ID: {participant_id}"
            )
            self.status_var.set("No matching participant found.")
            return

        self._show_records([record])
        self._load_record_into_form(record)
        self.status_var.set(f"Showing participant {participant_id}.")

    def update_participant(self):
        record = self._read_form()
        if record is None:
            return

        old_id = self.selected_id or record["id"]
        if old_id not in self.participants:
            messagebox.showinfo(
                "Update", "Search for or select an existing participant first."
            )
            return

        if record["id"] != old_id and record["id"] in self.participants:
            messagebox.showerror(
                "Duplicate ID", "Another participant already uses this ID."
            )
            return

        del self.participants[old_id]
        self.participants[record["id"]] = record
        self.display_all()
        self.clear_form()
        self.status_var.set(f"Participant {record['id']} updated successfully.")

    def remove_participant(self):
        participant_id = self.selected_id or self.id_entry.get().strip()
        if not participant_id or participant_id not in self.participants:
            messagebox.showinfo(
                "Remove", "Select or search for an existing participant first."
            )
            return

        confirmed = messagebox.askyesno(
            "Confirm Removal",
            f"Remove participant {participant_id}?",
        )
        if not confirmed:
            return

        del self.participants[participant_id]
        self.display_all()
        self.clear_form()
        self.status_var.set(f"Participant {participant_id} removed.")

    def display_all(self):
        records = sorted(
            self.participants.values(), key=lambda item: item["id"].lower()
        )
        self._show_records(records)
        self.status_var.set("Displaying all registered participants.")

    def _show_records(self, records):
        self.listbox.delete(0, tk.END)
        for record in records:
            line = (
                f"{record['id']:<18.18} "
                f"{record['name']:<22.22} "
                f"{record['sport']:<15.15} "
                f"{record['age']:<6} "
                f"{record['participation']:<12}"
            )
            self.listbox.insert(tk.END, line)
        self.count_var.set(f"Participants: {len(self.participants)}")

    def load_selected(self, _event=None):
        selection = self.listbox.curselection()
        if not selection:
            return

        # The displayed list may be filtered by search, so use the visible row's ID.
        row = self.listbox.get(selection[0])
        participant_id = row.split()[0]
        record = self.participants.get(participant_id)
        if record:
            self._load_record_into_form(record)

    def _load_record_into_form(self, record):
        self.selected_id = record["id"]
        self._replace_entry(self.id_entry, record["id"])
        self._replace_entry(self.name_entry, record["name"])
        self._replace_entry(self.age_entry, str(record["age"]))
        self.sport_var.set(record["sport"])
        self.participation_var.set(record["participation"])

    @staticmethod
    def _replace_entry(entry, value):
        entry.delete(0, tk.END)
        entry.insert(0, value)

    def clear_form(self):
        self.selected_id = None
        for entry in (self.id_entry, self.name_entry, self.age_entry):
            entry.delete(0, tk.END)
        self.sport_var.set(SPORTS[0])
        self.participation_var.set("Individual")
        self.listbox.selection_clear(0, tk.END)
        self.id_entry.focus_set()


if __name__ == "__main__":
    root = tk.Tk()
    app = SportsEventApp(root)
    root.mainloop()
