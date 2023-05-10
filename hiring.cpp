#include <bits/stdc++.h>
using namespace std;
int main()
{
  int n;
  cout << "Enter no of candidate to hire ";
  cin >> n;
  int arr[n];
  string name[n];
  string skill[n];
  string skill2[n];
  for (int i = 0; i < n; i++)
  {
    int s = 1;
    cout << "Enter the name " << endl;
    cin >> name[i];
    cout << "Enter the skill " << endl;
    cin >> skill[i];
    cout << "Enter the skill2 " << endl;
    cin >> skill2[i];
    if (skill[i] == "english")
    {
      s = s + 2;
    }
    if (skill2[i] == "coding")
    {
      s = s + 1;
    }
    cout << "Skill score is " << s << endl;
    arr[i] = s;
  }
  cout << "skill score of all candidate are " << endl;
  for (int i = 0; i < n; i++)
  {
    cout << arr[i] << " ";
  }
  cout << endl;
  int cost;
  int wcost;
  int cost_hire = 100;
  int cost_fire = 50;
  int best = arr[0];
  cost += cost_hire;
  int day = 1;
  for (int i = 1; i < n; i++)
  {
    if (arr[i] > best)
    {
      cout << "candidate hired " << arr[i] << "candidate fired " << best << endl;
      best = arr[i];
      cost += cost_hire + cost_fire;
    }
  }
  cout << "Randomized "
       << "candidate hired " << best << " " << cost << endl;
  sort(arr, arr + n);
  best = arr[0];
  for (int i = 1; i < n; i++)
  {
    if (arr[i] > best)
    {
      cout << "candidate hired " << arr[i] << "candidate fired " << best << endl;
      best = arr[i];
      cost += cost_hire + cost_fire;
    }
  }
  cout << "Worst case "
       << "candidate hired " << best << " " << cost << endl;
}
