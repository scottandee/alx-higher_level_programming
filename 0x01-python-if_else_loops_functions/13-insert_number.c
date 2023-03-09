#include "lists.h" 
/**
  * insert_node - this inserts a node at the middle of the list
  * @head: this is the first element in the linked list
  * @number: this is the number to be added
  * Return: the address of the new_node or null if it failed
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	new_node->n = number;
	new_node->next = NULL;
	if (temp == NULL || number < temp->n)
	{
		new_node->next = temp;
		*head = new_node;
	}
	else
	{
		while (temp->next != NULL && temp->next->n < number)
		{
			temp = temp->next;
		}
		new_node->next = temp->next;
		temp->next = new_node;
	}
	return(new_node);
}
