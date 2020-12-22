#include <iostream>
#include <vector>
#include <stack>
#include <stdlib.h> 
#include <math.h>

using namespace std;
#define infinity 9999999

//cau truc du lieu cho 1 diem
struct Point
{
	int x;
	int y;
};

Point p0;

//thuat toan counterclockwise
//=0 thang hang
//<0 nguoc chieu kiem dong ho
//>0 chieu kim dong ho

int CWW(Point a, Point b, Point c)
{
	int val = (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x);

	if (val == 0)
	{
		return 0;
	}
	return (val > 0) ? 1 : 2;
}

float dist(Point p1, Point p2)
{
	return sqrt((p1.x - p2.x) * (p1.x - p2.x) +
		(p1.y - p2.y) * (p1.y - p2.y)
	);
}

int compareX(const void* a, const void* b)
{
	Point* p1 = (Point*)a, * p2 = (Point*)b;
	return (p1->x - p2->x);
}

int compareY(const void* a, const void* b)
{
	Point* p1 = (Point*)a, * p2 = (Point*)b;
	return (p1->y - p2->y);
}

float bruteForce(Point P[], int n)
{
	float min = FLT_MAX;
	for (int i = 0; i < n; ++i)
		for (int j = i + 1; j < n; ++j)
			if (dist(P[i], P[j]) < min)
				min = dist(P[i], P[j]);
	return min;
}

float min(float x, float y)
{
	return (x < y) ? x : y;
}

float stripClosest(Point strip[], int size, float d)
{
	float min = d;  

	for (int i = 0; i < size; ++i)
		for (int j = i + 1; j < size && (strip[j].y - strip[i].y) < min; ++j)
			if (dist(strip[i], strip[j]) < min)
				min = dist(strip[i], strip[j]);

	return min;
}

bool onSegment(Point p, Point q, Point r)
{
	if (q.x <= max(p.x, r.x) && 
		q.x >= min(p.x, r.x) && 
		q.y <= max(p.y, r.y) && 
		q.y >= min(p.y, r.y))
	{
		return true;
	}

	return false;
}

bool doIntersect(Point p1, Point q1, Point p2, Point q2)
{
	int o1 = CWW(p1, q1, p2);
	int o2 = CWW(p1, q1, q2);
	int o3 = CWW(p2, q2, p1);
	int o4 = CWW(p2, q2, q1);

	if (o1 != o2 && o3 != o4)
	{
		return true;
	}

	if (o1 == 0 && onSegment(p1, p2, q1))
	{
		return true;
	}

	if (o2 == 0 && onSegment(p1, q2, q1))
	{
		return true;
	}

	if (o3 == 0 && onSegment(p2, p1, q2))
	{
		return true;
	}

	if (o4 == 0 && onSegment(p2, q1, q2))
	{
		return true;
	}

	return false;
}

bool isInside(Point polygon[], int n, Point p)
{ 
	if (n < 3)  return false;

	Point extreme = { infinity, p.y };
 
	int count = 0, i = 0;
	do
	{
		int next = (i + 1) % n;

		if (doIntersect(polygon[i], polygon[next], p, extreme))
		{
			if (CWW(polygon[i], p, polygon[next]) == 0)
				return onSegment(polygon[i], p, polygon[next]);

			count++;
		}
		i = next;
	} while (i != 0);

	
	return count & 1;
}


void Jarvis_convexHull(Point points[], int n)
{
	if (n < 3) return;

	
	vector<Point> hull;

	int l = 0;
	for (int i = 1; i < n; i++)
		if (points[i].x < points[l].x)
			l = i;

	int p = l, q;
	do
	{
		hull.push_back(points[p]);

		q = (p + 1) % n;
		for (int i = 0; i < n; i++)
		{
			if (CWW(points[p], points[i], points[q]) == 2)
				q = i;
		} 
		p = q;

	} while (p != l); 

	// Print Result 
	for (int i = 0; i < hull.size(); i++)
		cout << "(" << hull[i].x << ", "
		<< hull[i].y << ")\n";
}


void main()
{
	
	/*
	//demo CWW

	*/

	/*
	//demo line intersect
	Point p1 = {1, 1}, q1 = {10, 1};
	Point p2 = {1, 2}, q2 = {10, 2};

	doIntersect(p1, q1, p2, q2)? cout << "Yes\n": cout << "No\n";

	p1 = {10, 0}, q1 = {0, 10};
	p2 = {0, 0}, q2 = {10, 10};
	doIntersect(p1, q1, p2, q2)? cout << "Yes\n": cout << "No\n";

	p1 = {-5, -5}, q1 = {0, 0};
	p2 = {1, 1}, q2 = {10, 10};
	doIntersect(p1, q1, p2, q2)? cout << "Yes\n": cout << "No\n";
	*/

	
	//demo inside or out side
	/*
	Point polygon1[] = {{0, 0}, {10, 0}, {10, 10}, {0, 10}};
	int n = sizeof(polygon1)/sizeof(polygon1[0]);
	Point p = {20, 20};
	isInside(polygon1, n, p)? cout << "Yes \n": cout << "No \n";

	p = {5, 5};
	isInside(polygon1, n, p)? cout << "Yes \n": cout << "No \n";

	Point polygon2[] = {{0, 0}, {5, 5}, {5, 0}};
	p = {3, 3};
	n = sizeof(polygon2)/sizeof(polygon2[0]);
	isInside(polygon2, n, p)? cout << "Yes \n": cout << "No \n";

	p = {5, 1};
	isInside(polygon2, n, p)? cout << "Yes \n": cout << "No \n";

	p = {8, 1};
	isInside(polygon2, n, p)? cout << "Yes \n": cout << "No \n";

	Point polygon3[] =  {{0, 0}, {10, 0}, {10, 10}, {0, 10}};
	p = {-1,10};
	n = sizeof(polygon3)/sizeof(polygon3[0]);
	isInside(polygon3, n, p)? cout << "Yes \n": cout << "No \n";
	*/

	/*
	//demo convex hull - Jarvis
	Point points[] = { {0, 3}, {2, 2}, {1, 1}, {2, 1},
					  {3, 0}, {0, 0}, {3, 3} };
	int n = sizeof(points) / sizeof(points[0]);
	Jarvis_convexHull(points, n);
	*/


}