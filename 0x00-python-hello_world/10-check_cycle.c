#include "lists.h"

/**
  * check_cycle - checks if a singly linked list has a cycle in it
  * @list: this is the first element of the singly linked list
  * Return: 0 if there is no cycle, 1 if there's a cycle
  */
int check_cycle(listint_t *list)
{	
	listint *current;

	current = head;

	if (list == NULL)
	{
		return (0);
	}
	while (current != NULL)
	{
		if (temp->next == list)
			return (1)
		current = current->next;
	}
	return (0);

}
