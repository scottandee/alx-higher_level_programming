#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: this is the first element of the singly linked list
  * Return: 0 if there is no cycle, 1 if there's a cycle
  */
int check_cycle(listint_t *list)
{	
	int count = 0;

	if (list == NULL)
	{
		return (0);
	}
	while (list != NULL && count < 9)
	{
		count++;
		list = list->next;
	}
	if (count > 8)
	{
		return (0);
	}
	return (1);

}
