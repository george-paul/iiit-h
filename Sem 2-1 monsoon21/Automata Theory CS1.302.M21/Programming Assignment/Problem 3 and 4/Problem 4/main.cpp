#include <iostream>
#include <stack>
#include <vector>
#include <queue>
using namespace std;

struct state {
    int sname; //state name
    vector<char>inputs;  //All the inputs given to a particular state.
    vector<state*> destState; //Destination states corresponding to above inputs.
};

struct nfa{
    state* initstate; //Store Initial state of the NFA
    state* finalstate; //Store Final state of the NFA.
};

stack<nfa> st;//To maintain records of the NFA 
int s_counter=0;// To give names to all the states.
vector<int>visited;

bool checkOperator(char c)
{
    if(c=='+'||c=='.'||c=='|'||c=='*')return true;
    else return false;
}
bool checkOperand(char c)
{
    if(c>='a'&&c<='z')return true;
    else if(c>='0'&&c<='9')return true;
    else if(c>='A'&&c<='Z')return true;
    else return false;
}
int precedence(char c)
{
    if(c=='*')return 3;
    else if(c=='.')return 2;
    else if(c=='+'||c=='|')return 1;
    else return -1;
}
string toPostfix(string exp)
{
    string post="";
    stack<char>stk;
    for(int i=0;i<exp.length();i++)
    {
        if(exp[i]==' ')continue;
        else if(checkOperator(exp[i]))
        {
            while(!stk.empty() && stk.top()!='(' && precedence(stk.top()) >= precedence(exp[i]))
            {
                post+=stk.top();
                stk.pop();
            }
            stk.push(exp[i]);
        }
        else if(checkOperand(exp[i])) post+=exp[i];
        else if (exp[i]=='(') stk.push(exp[i]);
		else if(exp[i]==')') 
		{
			while(!stk.empty() && stk.top()!= '(') {
				post+=stk.top();
                stk.pop();
			}
			stk.pop();
		}
	}
	while(!stk.empty())
    {
		post+=stk.top();
		stk.pop();
	}
    return post;
}

state* createNode(int i)
{
    //cout<<"state number: "<<i<<"created";
    state* t=new state;
    t->sname=i; //initialise state names
    return t;
}
nfa* createNfa(state* p, state* q)  //p and q have the initial state and final state of the nfa.
{
    nfa* nfa1=new nfa; 
    nfa1->initstate = p; //initialize the initial state.
    nfa1->finalstate = q; //initialize the final state.
    return nfa1;
}
void pushInput(char c)
{
    state* p= createNode(s_counter);s_counter++; //create the first state
    state* q= createNode(s_counter);s_counter++; //create the second state
    p->inputs.push_back(c); //inserting the input.
    p->destState.push_back(q); // state on taking input reaches state q.
    nfa* tempNFA= createNfa(p,q); //create the nfa with these two states.
    st.push(*tempNFA); // push down the stack
}
void unions()
{
    nfa nfa1=st.top();st.pop(); //pop out the top nfa of the stack
    nfa nfa2=st.top();st.pop(); //pop out the second nfa of the stack

    // cout<<nfa1.initstate->sname<<" "<<nfa1.finalstate->sname<<endl;
    // cout<<nfa2.initstate->sname<<" "<<nfa2.finalstate->sname<<endl;

    state* t=createNode(s_counter);s_counter++; //create state t 
    state* t1=createNode(s_counter);s_counter++; //create state t1

    t->inputs.push_back('E'); //inserting the input E.
    t->destState.push_back(nfa1.initstate);//state t on input E reaches initial state of nfa1

    t->inputs.push_back('E'); //inserting the input E.
    t->destState.push_back(nfa2.initstate); //state t on input E reaches initial state of nfa2

    nfa1.finalstate->inputs.push_back('E'); //inserting the input E to finalstate of nfa1
    nfa1.finalstate->destState.push_back(t1); //final state of nfa1 on input E reaches t1

    nfa2.finalstate->inputs.push_back('E'); //inserting the input E to finalstate of nfa2
    nfa2.finalstate->destState.push_back(t1); //finalstate of nfa2 on input E reaches t1

    nfa* tNfa=createNfa(t,t1); //create nfa with t as initial state and t1 as final state.
    st.push(*tNfa);
}
void concatenate()
{
    nfa nfa1=st.top();st.pop(); //pop out the top nfa of the stack
    nfa nfa2=st.top();st.pop(); //pop out the second nfa of the stack

    // cout<<nfa1.initstate->sname<<" "<<nfa1.finalstate->sname<<endl;
    // cout<<nfa2.initstate->sname<<" "<<nfa2.finalstate->sname<<endl;

    //to perform nfa2.nfa1
    nfa2.finalstate->inputs.push_back('E'); //finalstate on input E 
    nfa2.finalstate->destState.push_back(nfa1.initstate); //reaches initialstate of nfa1

    //create nfa with initalstate of nfa2 and finalstate of nfa1
    nfa* tnfa=createNfa(nfa2.initstate,nfa1.finalstate);
    st.push(*tnfa);//push down the stack
}
void closure()
{
    nfa nfa1=st.top();st.pop(); //pop out the top of stack to perform closure.

    //cout<<nfa1.initstate->sname<<" "<<nfa1.finalstate->sname<<endl;
    //cout<<nfa2.initstate->sname<<" "<<nfa2.finalstate->sname<<endl;

    state* t=createNode(s_counter);s_counter++; //create state t
    state* t1=createNode(s_counter);s_counter++; //create state t1

    t->inputs.push_back('E'); //t('E')->nfa1.initalstate
    t->destState.push_back(nfa1.initstate);

    t->inputs.push_back('E'); //t('E')->t1
    t->destState.push_back(t1);

    nfa1.finalstate->inputs.push_back('E'); //nfa1.finalstate('E')->nfa1.initalstate
    nfa1.finalstate->destState.push_back(nfa1.initstate);

    nfa1.finalstate->inputs.push_back('E'); //nfa1.finalstate('E')->t1
    nfa1.finalstate->destState.push_back(t1);

    nfa* tNfa=createNfa(t,t1); //create nfa with t and t1 and init and fin state
    st.push(*tNfa);//push down the stack.
}
void traverseNfa(state* s)
{
    char graph[s_counter][s_counter];
    for(int i=0;i<s_counter;i++)
    {
        for(int j=0;j<s_counter;j++)
        {
            graph[i][j]='-';
        }
    }
    queue<state*>q;
    q.push(s);
    while(!q.empty())
    {
        state* st=q.front();
        q.pop();
        for(int i=0;i<st->inputs.size();i++)
        {
            graph[st->sname][st->destState[i]->sname]=st->inputs[i];
            cout<<"State "<<st->sname<<" on input "<<st->inputs[i]<<" reaches state "<<st->destState[i]->sname<<endl;
            if(visited[st->destState[i]->sname]==0)q.push(st->destState[i]);
        }
        visited[st->sname]=1;
    }
    cout<<"\n\n   ";
    for(int i=0;i<s_counter;i++)cout<<i<<"\t";
    cout<<endl;
    for(int i=0;i<s_counter;i++)
    {
        cout<<i<<"  ";
        for(int j=0;j<s_counter;j++)
        {
            cout<<graph[i][j]<<"\t";
        }
        cout<<"\n";
    }
}
void initializeVector() //initializeing the visited vector.
{
    for(int i=0;i<s_counter-1;i++)
    {
        visited.push_back(0);
    }
}
int main()
{
    string regExp;

    cout<<"Input the Regular Expression:";
    getline (cin, regExp);

    string postfix= toPostfix(regExp);
    cout<<"postfix Expression corresponding to the given Regular Expression is: "<<postfix<<endl;

    for(int i=0;i<postfix.length();i++)
    {
        if(postfix[i]=='+'||postfix[i]=='|') unions();
        else if (postfix[i]=='.') concatenate();
        else if(postfix[i]=='*') closure();
        else pushInput(postfix[i]);
    }

    nfa finalNfa= st.top();
    st.pop();
    
    cout<<"Initial State of NFA: "<<finalNfa.initstate->sname<<endl;
    cout<<"Final State of NFA: "<<finalNfa.finalstate->sname<<"\n\n";

    initializeVector();
    traverseNfa(finalNfa.initstate);
    return 0;
}