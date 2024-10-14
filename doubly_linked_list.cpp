#include<iostream>
using namespace std;

class Node{
    public:


        int bit;
        Node *prev;
        Node *next;

        
        Node(int bit){
            this->bit=bit;
            this->prev=NULL;
            this->next=NULL;
        }

    
};

void binary(int num,Node* tail){
    Node* mover=tail;
    while(num>0){
        num/=2;
        Node* temp=new Node(num%2);
        mover->prev=temp;
        temp->next=mover;
        mover=temp;
    }
    
}

void display(Node* tail){
    Node* mover = tail;

    while(mover->prev != NULL){
        mover=mover->prev;
    }
    cout<<"\n Number's binary form is = ";
    while(mover != NULL){    
        cout<<mover->bit;    
        mover = mover -> next;
    }
    cout<<"\n";
}


void ones_Compliment(Node* tail){
    Node* mover = tail;

    while(mover->prev != NULL){
        mover=mover->prev;
    }
    while(mover != NULL){
        if(mover->bit==0){
            cout<<1;
        }else{
            cout<<0;
        }
        mover = mover -> next;

    }
}


void twos_Compliment(Node* tail){


}


int main(){
    cout<<"Enter The First Number = \n";
    int num_1,num_2;cin>>num_1;
    cout<<"Enter The Second Number = \n";
    cin>>num_2;
    Node* tail_1=new Node(num_1%2);
    Node* tail_2=new Node(num_2%2);

    binary(num_1,tail_1);
    binary(num_2,tail_2);
    cout<<"1st Number in binary IS \n";
    display(tail_1);
    cout<<"2nd Number in "
    display(tail_2);
    cout<<"For 1st Number ";
    ones_Compliment(tail_1);
    cout<<"For 2nd Number ";
    ones_Compliment(tail_2);



}


