#include "lists.h"
#include "stdlib.h"
/**
 *insert_node - inserts a node in a sorted singly linked lis
 *
 *@head: a pointer to the head pointer of the list
 *@number: the number to set s value of new node
 *Return: the address of the new node or NULL if failed
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node, *temp;

	new_node = (listint_t *)malloc(sizeof(listint_t));
	if (*head == NULL && new_node)
	{
		new_node->n = number;
		new_node->next = NULL;
		return (new_node);
	}
	temp = *head;
	while (temp && new_node)
	{
		if (temp->next == NULL)
		{
			new_node->n = number;
			new_node->next = NULL;
			temp->next = new_node;
			return (new_node);
		}
		if (temp->next->n > number)
		{
			new_node->n = number;
			new_node->next = temp->next;
			temp->next = new_node;
			return (new_node);
		}
		temp = temp->next;
	}
	return (NULL);
}
