#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: this is the first element of the singly linked list
  * Return: 0 if there is no cycle, 1 if there's a cycle
  */
int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	fast = list->next;
	slow = list;

	if (list == NULL)
	{
		return (0);
	}
	while (fast != NULL && fast->next != NULL && slow != NULL)
	{
		if (fast == slow)
			return (1);
		fast = fast->next->next;
		slow = slow->next;
	}
	return (0);

}
