#include <iostream>
using namespace std;

class Node {
public:
    int PRN_NO;
    string Name;
    Node *next;

    
    Node(int PRN_NO, const string &Name) {
        this->PRN_NO = PRN_NO;
        this->Name = Name;
        this->next = nullptr;
    }

    
    ~Node() {
        
        while (next != nullptr) {
            Node* temp = next;
            next = next->next;
            delete temp;
        }
    }
};

void addMembers(Node* head) {
    int n;
    cout << "Enter the number of members you want to add: ";
    cin >> n;
    Node* temp = head;

    while (n > 0) {
        string Name;
        int PRN_NO;
        cout << "Enter PRN_NO and Name: ";
        cin >> PRN_NO >> Name;
        temp->next = new Node(PRN_NO, Name);
        temp = temp->next;
        n--;
    }
}

void appendMember(Node* head) {
    Node* temp = head;
    while (temp->next != nullptr) {
        temp = temp->next;
    }
    temp->next = new Node(763542, "NEW");
}

void displayMembers(const Node* head) {
    const Node* temp = head;
    int count = 0;
    while (temp != nullptr) {
        cout << "Member " << (count + 1) << ":" << endl;
        cout << "PRN_NO: " << temp->PRN_NO << ", Name: " << temp->Name << endl;
        temp = temp->next;
        count++;
    }
}

void countMembers(const Node* head) {
    const Node* temp = head;
    int count = 0;
    while (temp != nullptr) {
        count++;
        temp = temp->next;
    }
    cout << "Total number of students: " << count << endl;
}

void deleteMember(Node* &head, const string &Name) {
    Node* temp = head;
    Node* prev = nullptr;

    while (temp != nullptr) {
        if (temp->Name == Name) {
            if (prev == nullptr) { 
                head = temp->next;
            } else {
                prev->next = temp->next;
            }
            delete temp;
            cout << "Member deleted." << endl;
            return;
        }
        prev = temp;
        temp = temp->next;
    }
    cout << "Member not found." << endl;
}

int main() {
    Node* head = new Node(323, "Na");
    int choice;

    do {
        cout << "\nMenu:" << endl;
        cout << "1. Add members" << endl;
        cout << "2. Delete a member" << endl;
        cout << "3. Display total number of students" << endl;
        cout << "4. Display all members" << endl;
        cout << "5. Exit" << endl;
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice) {
            case 1:
                addMembers(head);
                break;
            case 2: {
                string name;
                cout << "Enter the name of the member to delete: ";
                cin >> name;
                deleteMember(head, name);
                break;
            }
            case 3:
                countMembers(head);
                break;
            case 4:
                displayMembers(head);
                break;
            case 5:
                cout << "Exiting..." << endl;
                break;
            default:
                cout << "Invalid choice. Please try again." << endl;
        }
    } while (choice != 5);

  
    delete head;

    return 0;
}
