#include <bits/stdc++.h>
using namespace std;

class Node {
public:
    string position;
    string name;
    Node *next;


    public:
        Node(string position,string name){
            this->position=position;
            this->name=name;
            this->next=NULL;
        }
    
    
};

void create__ll(Node* head,int n){
    Node* mover = head;
    string g,h;
    while(n>1){
        cout<<"Enter data position\n";
        cin>>g;
        cout<<"Enter data name\n";
        cin>>h;
        Node* temp = new Node(g,h);
        mover->next=temp;
        mover=temp;
        n--;
    }
}

void Display(Node* head){
    Node* temp=head;
    while(temp!=NULL){
        cout<<temp->position<<" "<<temp->name<<" "<<"\n";
        temp=temp->next;
    }
}

void Number(Node* head){
    int f=0;
    Node* temp=head;
    while(temp!=NULL){
        f++;
        temp=temp->next;
    }
    cout<<"There are "<<f<<" Members in Pinnacle Club."<<"\n";
}

void Reverse_Display(Node* head){
    if (head == nullptr) {
        return;
    }
    
    Reverse_Display(head->next);
    
    cout<<head->position<<" "<<head->name<<"\n";

}

void Delete_member(Node* head){
    cout<<"Enter Name of Member To be Deleted:-\n";
    string h;cin>>h;
    Node* mover =head;
    Node* temp=head;
    while(mover!=NULL){
        if(mover->name==h&&mover->position=="member"){
            temp->next=mover->next;
            delete mover;
            cout<<"!!!!Member Succesfully Deleted!!!!";
            break;
        }
        mover=mover->next;
        if(mover->name!=h){
            temp=temp->next;
        }
    }
}

void Delete_secratory(Node* head){
    cout<<"Enter Name of Secratory To be Deleted:-\n";
    string h;cin>>h;
    Node* mover =head;
    Node* temp=head;
    while(mover!=NULL){
        if(mover->name==h){
            temp->next=mover->next;
            delete mover;
            cout<<"!!!!Secratory Succesfully Deleted!!!!";
            break;
        }
        mover=mover->next;
        if(mover->name!=h){
            temp=temp->next;
        }
    }
}

void seceratory(Node* head){
    Node* mover=head;
    while(mover->next!=NULL){
        mover=mover->next;
    }
    cout<<"Enter New Secratory Name\n";
    string d;cin>>d;
    Node* temp=new Node("Secratory",d);
    mover->next=temp;
}

void president(Node* &head){
    cout<<"Enter Name of New President\n";
    string b;cin>>b;
    Node* temp=new Node("President",b);
    temp->next=head;
    head->position="member";
    head=temp;
}

void Delete_president(Node* head){
    Node* temp=head;
    head=head->next;
    delete temp;
    cout<<"President Succesfully Deleted. \n";
    cout<<"!!!!Club cannot be without president!!!!\n";
    president(head);
}
void Concatinate(Node* head,Node* head1){
    Node* temp=head1;
    Node* mover=head;
    while(mover->next!=NULL){
        mover=mover->next;
    }
    mover->next=temp;
}

int main(){
    cout<<"Enter number of elements in linked list\n";
    int n;cin>>n;
    string f,fn;
    cout<<"Enter data position\n";
    cin>>f;
    cout<<"Enter data name\n";
    cin>>fn;
    Node* head=new Node(f,fn);
    create__ll(head,n);
    
    
    while(true){
        cout<<"\n\nChoose any Operation\n\n";
        cout<<" 1. Add President\n";
        cout<<" 2. Insert Secratory\n";
        cout<<" 3. Delete President\n";
        cout<<" 4. Delete Secratory\n";
        cout<<" 5. Delete Member\n";
        cout<<" 6. Number of Students in Club\n";
        cout<<" 7. Display All Members\n";
        cout<<" 8. Display All Members in Reverse Order\n";
        cout<<" 9. Concatinate New List\n";
        cout<<" 10. EXIT\n";
        int j;cin>>j;

        if(j==1){
            president(head);
        }else if(j==2){
            seceratory(head);
        }else if(j==3){
            Delete_president(head);
        }else if(j==4){
            Delete_secratory(head);
        }else if(j==5){
            Delete_member(head);
        }else if(j==6){
            Number(head);
        }else if(j==7){
            Display(head);
        }else if(j==8){
            Reverse_Display(head);
        }else if(j==9){
            cout<<"Enter total number of people to be concatinate\n";
            int m;cin>>m;
            cout<<"Enter president name of new list\n";
            string g;cin>>g;
            Node* head1=new Node("president",g);
            create__ll(head1,m);
            Concatinate(head,head1);

        }else if(j==10){
            break;
        }else{
            cout<<"\n\nEnter A Valid Option\n\n";
        }
    }
    return 0;
}
