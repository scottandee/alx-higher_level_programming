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
	/*int i = 0, j;*/

	temp = *head;
	new_node = malloc(sizeof(listint_t));
	if (new_node == NULL)
	{
		return (NULL);
	}
	/*new_node->n = number;
	new_node->next = NULL;

	while (temp != NULL)
	{
		i++;
		temp = temp->next;
	}
	temp = *head;
	for (j = 0; j < i / 2; i++)
	{
		temp = temp->next;
	}
	new_node->next = temp;
	return (new_node);*/

	if (temp == NULL)
	{
		*head = new_node;
	}
	else
	{
		while (temp->next != NULL)
		{
			temp = temp->next;
		}
		temp->next = new_node;
	}
	new_node->n = number;
	return (*head);
}
