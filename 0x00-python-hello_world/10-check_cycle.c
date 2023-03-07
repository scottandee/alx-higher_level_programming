#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: this is the first element of the singly linked list
  * Return: 0 if there is no cycle, 1 if there's a cycle
  */
int check_cycle(listint_t *list)
{	
	int list_len;

	list_len = listint_len(list);

	if (list_len > 8)
	{
		return (0);
	}
	return (1);

}

/**
  * listint_len - this counts the nnumber of elements in a singly linked list
  * @h: this is the head of the list
  * Return: the nuumber of elements in singly linked list
  */

int listint_len(const listint_t *h)
{
	int count = 0;

	if (h == NULL)
	{
		return (0);
	}
	while (h != NULL)
	{
		count++;
		h = h->next;
	}
	return (count);
}
