#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define maxN 100
#define ALPHABET_COUNT 26


struct DFA
{
	int N;						// number of states
	int A;						// number of accept states
	vector<int> a;				// list of accept states
	int K;						// number of transitions
	vector<vector<int>> t;		// transition table // also t[N+1][any] gives the initial state
	int initState;
};

DFA oldD;
DFA newD;
int marks[maxN][maxN];			// table filling method table
vector<vector<int>> equiv;		// equivalent states


// takes input for the program
void inputOldDFA()
{
	cin>>oldD.N>>oldD.A>>oldD.K;
	int accState;
	for(int i = 0; i<oldD.A; i++)
	{
		cin>>accState;
		oldD.a.push_back(accState);
	}

	// initialize the old DFA state table
	vector<int> x;
	// generate list of ALPHABET_COUNT -1's
	for(int i = 0; i<ALPHABET_COUNT; i++)
		x.push_back(-1);
	for(int i = 0; i<oldD.N; i++)
		oldD.t.push_back(x);

	char xa;
	int s1, s2;
	for(int i = 0; i<oldD.K; i++)
	{
		cin >> s1 >> xa >> s2;
		if(i == 0)
		{
			oldD.initState = s1;
		}
		oldD.t[s1][xa-'a'] = s2;
	}
}

// for now, only oldDFA shows
void showDFA()
{
	cout<<"\nno of states(N)= "<<oldD.N
		<<"\nno of accepting states(A)= "<<oldD.A<<endl;
	for(int i = 0; i<oldD.A; i++)
	{
		cout<<oldD.a[i]<<", ";
	}
	cout<<"\n---\nno of transitions(K)= "<<oldD.K<<endl;
	for (int i = 0; i<oldD.N; i++)
	{
		for(int j = 0; j<ALPHABET_COUNT; j++)
		{
			if(oldD.t[i][j] != -1)
			{
				cout<<i<<" --"<<(char)(j +'a')<<"--> "<<oldD.t[i][j]<<endl;
			}
		}
	}
	cout<<"---\ninitial state is "<<oldD.initState<<endl;
}

// checks whether s is a final state
bool isFinal(int s)
{
	for(int i = 0; i<oldD.a.size(); i++)
	{
		if(s == oldD.a[i]) return true;
	}
	return false;
}

// marking for myhill-nerode table filling method
void markUnique()
{
	// mark final-nonfinal pairs and initialise array
	for(int i = 0; i<oldD.N; i++)
	{
		for(int j = 0; j<oldD.N; j++)
		{
			if(j>=i)
			{
				marks[i][j] = 2;				// unused values
			}
			else if(( isFinal(i) && !isFinal(j) )||( !isFinal(i) && isFinal(j) ))
			{
				marks[i][j] = 1;
			}
			else
			{
				marks[i][j] = 0;
			}
		}
	}
	int x,y;
	bool toMark = true;
	// mark equal transition states (step 3)
	while(toMark)					// while there are still pairs to mark
	{
		toMark = false;				// assume last go around
		for(int i = 0; i<oldD.N; i++)
		{
			for(int j = i+1; j<oldD.N; j++)
			{
				if(marks[j][i] == 0)
				{
					for(int k=0;k<ALPHABET_COUNT;k++)
					{
						x = oldD.t[i][k];
						y = oldD.t[j][k];
						if(marks[x][y] == 1 || marks[y][x] == 1)
						{
							marks[j][i] = 1;
							toMark = true;					// go around again since the table changed
						}
					}
				}
			}
		}
	}
}

// for debugging
void showMarks()
{
	for(int i = 0; i<oldD.N; i++)
	{
		for(int j = 0; j<oldD.N; j++)
		{
			cout<<marks[i][j]<<":"<<i<<j<<"\t";	
		}
		cout<<endl;
	}
}

// for debugging
void showEquiv()
{
	for(int i = 0; i<equiv.size(); i++)
	{
		for(int j = 0; j<equiv[i].size(); j++)
		{
			cout<<equiv[i][j]<<"\t";
		}
		cout<<endl;
	}
}

// insert the a=b equivalence
void insertEquiv(int a, int b)
{
	// search for an existing equivalence
	for(int i = 0; i<equiv.size(); i++)
	{
		// a present
		if(find(equiv[i].begin(), equiv[i].end(), a) != equiv[i].end())
		{
			// only a present
			if(find(equiv[i].begin(), equiv[i].end(), b) == equiv[i].end())
			{
				equiv[i].push_back(b);
				return;
			}
			// both present
			else
				return;
		}
		// b present
		else if(find(equiv[i].begin(), equiv[i].end(), b) != equiv[i].end())
		{
			// only b present
			if(find(equiv[i].begin(), equiv[i].end(), a) == equiv[i].end())
			{
				equiv[i].push_back(a);
				return;
			}
			// both present
			else
				return;
		}
	}
	// if none found then add one with a and b
	equiv.push_back({a,b});
}

// fill the equivalence class list using the marks
void fillEquiv()
{
	for(int i = 0; i<oldD.N; i++)
	{
		for (int j = 0; j<oldD.N; j++)
		{	
			if(marks[i][j] == 0)
				insertEquiv(i, j);
		}
	}
	// if any states don't appear in any equiv then put them in a class of their own
	for(int a = 0; a<oldD.N; a++)
	{
		bool found = false;
		for(int i = 0; i<equiv.size(); i++)
		{
			if(find(equiv[i].begin(), equiv[i].end(), a) != equiv[i].end())
			{
				found = true;
				break;
			}
		}
		if(!found)
		{
			equiv.push_back({a});
		}
	}
	// showEquiv();			// debug
}

// for printing output
void showNFA()
{
	cout<<newD.N<<" "<<newD.A<<" "<<newD.K<<"\n";
	// accept states
	for(int i = 0; i<newD.A; i++)
	{
		cout<<newD.a[i]<<" ";
	}
	cout<<endl;
	for (int i = 0; i<newD.N; i++)
	{
		for(int j = 0; j<ALPHABET_COUNT; j++)
		{
			if(newD.t[i][j] != -1)
			{
				cout<<i<<" "<<(char)(j+'a')<<" "<<newD.t[i][j]<<endl;
			}
		}
	}
	cout<<"Minimized DFA initial state: "<<newD.initState<<endl;			// debug
}

// calculate the new transition for n on input a
int newTransition(int n, int a)
{
	for(int i = 0; i<equiv[n].size(); i++)
	{
		int oldTransition = oldD.t[equiv[n][i]][a];
		if(oldTransition == -1) continue;
		// old transition is in terms of old state numbers so make it in terms of new
		for(int j = 0; j<equiv.size(); j++)
		{
			if(find(equiv[j].begin(), equiv[j].end(), oldTransition) != equiv[j].end())
			{
				newD.K++;
				return j;
			}
		}
	}
	return -1;
}

// takes equiv and builds newD
void buildNewDFA()
{
	fillEquiv();
	newD.N = equiv.size();
	//transitions
	// for every state in newD
	for(int i = 0; i<newD.N; i++)
	{
		vector<int> v;
		// calculate each transition using the oldD
		for(int j = 0; j<ALPHABET_COUNT; j++)
		{
			v.push_back(newTransition(i,j));
		}
		newD.t.push_back(v);
	}
	// initial state
	for(int i = 0; i<equiv.size(); i++)
	{
		if(find(equiv[i].begin(), equiv[i].end(), oldD.initState) != equiv[i].end())
		{
			newD.initState = i;
			break;
		}
	}
	// accept states
	for(int i = 0; i<equiv.size(); i++)
	{
		for(int j = 0; j<equiv[i].size(); j++)
		{
			if(find(oldD.a.begin(), oldD.a.end(), equiv[i][j]) != oldD.a.end())
			{
				newD.A++;
				newD.a.push_back(i);
				break;
			}
		}
	}
}

int main()
{
	//freopen("./input.txt", "r", stdin);			// debug - input from file
	inputOldDFA();
	// showDFA();				// debug
	markUnique();
	// showMarks();			// debug
	buildNewDFA();
	showNFA();
	
	return 0;
}